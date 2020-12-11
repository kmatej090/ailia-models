import argparse
from pathlib import Path
import sys
import time

import cv2
import numpy as np
from PIL import Image

import ailia
from psgan.postprocess import PostProcess
from psgan.preprocess import PreProcess
from setup import setup_config

# Import original modules
sys.path.append("../../util")
from model_utils import check_and_download_models  # NOQA: E402
from webcamera_utils import adjust_frame_size, get_capture  # NOQA: E402

# ======================
# Parameters
# ======================
WEIGHT_PATH = "psgan.onnx"
MODEL_PATH = "psgan.onnx.prototxt"
FACE_PARSER_WEIGHT_PATH = "face_parser.onnx"
FACE_PARSER_MODEL_PATH = "face_parser.onnx.prototxt"
REMOTE_PATH = "https://storage.googleapis.com/ailia-models/psgan/"
face_parser_path = [FACE_PARSER_MODEL_PATH, FACE_PARSER_WEIGHT_PATH]

SOURCE_IMAGE_PATH = "images/non-makeup/xfsy_0106.png"
REFERENCE_IMAGE_PATH = "images/makeup"
SAVE_IMAGE_PATH = "output.png"
IMAGE_HEIGHT = 361
IMAGE_WIDTH = 361

# ======================
# Argument Parser Config
# ======================
parser = argparse.ArgumentParser(
    description="PSGAN: Pose and Expression Robust Spatial-Aware GAN for "
    + "Customizable Makeup Transfer"
)
parser.add_argument(
    "-v",
    "--video",
    metavar="VIDEO",
    default=None,
    help="The input video path. "
    + "If the VIDEO argument is set to 0, the webcam input will be used.",
)
parser.add_argument(
    "-s",
    "--savepath",
    metavar="SAVE_IMAGE_PATH",
    default=SAVE_IMAGE_PATH,
    help="Save path for the output image.",
)
parser.add_argument(
    "-b",
    "--benchmark",
    action="store_true",
    help="Running the inference on the same input 5 times "
    + "to measure execution performance. (Cannot be used in video mode)",
)
parser.add_argument(
    "--config_file",
    default="./configs/base.yaml",
    metavar="FILE",
    help="Path to config file",
)
parser.add_argument(
    "opts",
    help="Modify config options using the command-line.",
    default=None,
    nargs=argparse.REMAINDER,
)
parser.add_argument(
    "--source_path",
    default=SOURCE_IMAGE_PATH,
    metavar="FILE",
    help="Path to source image",
)
parser.add_argument(
    "--reference_dir", default=REFERENCE_IMAGE_PATH, help="Path to reference images"
)
parser.add_argument(
    "--device", default="cpu", help="Device used for inference",
)
parser.add_argument(
    "--onnx", action="store_true", help="Execute Onnx Runtime mode.",
)

args = parser.parse_args()
config = setup_config(args)

# ======================
# Main functions
# ======================


def _prepare_data(args, device, preprocess, image_type, frame=None):
    real = None
    mask = None
    diff = None
    crop_face = None
    if image_type == "source":
        image = Image.open(args.source_path).convert("RGB")
        image_input, _, crop_face = preprocess(image)
    elif image_type == "reference":
        paths = list(Path(args.reference_dir).glob("*"))
        image = Image.open(paths[0]).convert("RGB")
        image_input, _, _ = preprocess(image)
    elif image_type == "frame":
        image = frame
        image_input, _, crop_face = preprocess(image)
    else:
        raise ValueError

    if image_input:
        for i in range(len(image_input)):
            image_input[i] = image_input[i].to(device)

        real, mask, diff = image_input

    return image, real, mask, diff, crop_face


def _initialize_net(args):
    env_id = ailia.get_gpu_environment_id()
    print(f"env_id: {env_id}")
    if not args.onnx:
        net = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=env_id)
    else:
        import onnxruntime

        net = onnxruntime.InferenceSession(WEIGHT_PATH)

    return net


def _to_numpy(tensor):
    return (
        tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
    )


def _transfer(real_A, real_B, mask_A, mask_B, diff_A, diff_B, net):
    if not args.onnx:
        return net.predict(
            _to_numpy(real_A),
            _to_numpy(real_B),
            _to_numpy(mask_A),
            _to_numpy(mask_B),
            _to_numpy(diff_A),
            _to_numpy(diff_B),
        )
    else:
        inputs = {
            net.get_inputs()[0].name: _to_numpy(real_A),
            net.get_inputs()[1].name: _to_numpy(real_B),
            net.get_inputs()[2].name: _to_numpy(mask_A),
            net.get_inputs()[3].name: _to_numpy(mask_B),
            net.get_inputs()[4].name: _to_numpy(diff_A),
            net.get_inputs()[5].name: _to_numpy(diff_B),
        }
        return net.run(None, inputs)


def _postprocessing(out, source, crop_face, postprocess):
    out_sqz0 = out.squeeze(0)
    min_, max_ = out_sqz0.min(), out_sqz0.max()
    out_sqz0_nrm = (out_sqz0 - min_) / (max_ - min_ + 1e-5) * 255
    pil_img = Image.fromarray(np.transpose(out_sqz0_nrm, (1, 2, 0)).astype(np.uint8))
    source_crop = source.crop(
        (crop_face.left(), crop_face.top(), crop_face.right(), crop_face.bottom())
    )
    return postprocess(source_crop, pil_img)


def transfer_to_image():
    # Prepare input data
    device = args.device
    preprocess = PreProcess(config, device, args, face_parser_path)
    source, real_A, mask_A, diff_A, crop_face = _prepare_data(
        args, device, preprocess, "source"
    )
    _, real_B, mask_B, diff_B, _ = _prepare_data(args, device, preprocess, "reference")

    # Net initialize
    net = _initialize_net(args)

    # Inference
    print("Start inference...")
    if args.benchmark:
        print("BENCHMARK mode")
        for i in range(5):
            start = int(round(time.time() * 1000))
            out = _transfer(real_A, real_B, mask_A, mask_B, diff_A, diff_B, net)
            end = int(round(time.time() * 1000))
            print("\tailia processing time {} ms".format(end - start))
    else:
        out = _transfer(real_A, real_B, mask_A, mask_B, diff_A, diff_B, net)

    # Postprocessing
    postprocess = PostProcess(config)
    image = _postprocessing(out[0], source, crop_face, postprocess)
    image.save(args.savepath)
    print("Script finished successfully.")


def transfer_to_video():
    # Net initialize
    net = _initialize_net(args)

    device = args.device
    preprocess = PreProcess(config, device, args, face_parser_path)
    _, real_B, mask_B, diff_B, _ = _prepare_data(args, device, preprocess, "reference")
    postprocess = PostProcess(config)

    capture = get_capture(args.video)

    while True:
        ret, frame = capture.read()
        out = None
        if (cv2.waitKey(1) & 0xFF == ord("q")) or not ret:
            break

        # Prepare input data
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        in_frame, frame = adjust_frame_size(frame, IMAGE_HEIGHT, IMAGE_WIDTH)
        frame = Image.fromarray(frame)
        source, real_A, mask_A, diff_A, crop_face = _prepare_data(
            args, device, preprocess, "frame", frame
        )

        # Inference
        if real_A is not None:
            out = _transfer(real_A, real_B, mask_A, mask_B, diff_A, diff_B, net)

        # Postprocessing
        if out:
            image = _postprocessing(out[0], source, crop_face, postprocess)
            cv2.imshow("frame", cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))

    capture.release()
    cv2.destroyAllWindows()
    print("Script finished successfully.")


def main():
    # Check model files and download
    check_and_download_models(
        WEIGHT_PATH, MODEL_PATH, REMOTE_PATH,
    )
    check_and_download_models(
        FACE_PARSER_WEIGHT_PATH, FACE_PARSER_MODEL_PATH, REMOTE_PATH,
    )

    if args.video is not None:
        # Video mode
        transfer_to_video()
    else:
        # Image mode
        transfer_to_image()


if __name__ == "__main__":
    main()
