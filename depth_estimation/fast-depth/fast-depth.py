import os
import sys
import time

import cv2
import numpy as np
from PIL import Image

import ailia
from dataloaders.utils import val_transform
import utils_misc

# Import original modules.
sys.path.append("../../util")
from utils import get_base_parser, update_parser  # noqa: E402
from model_utils import check_and_download_models  # NOQA: E402
from webcamera_utils import get_capture, cut_max_square  # NOQA: E402

# Logger
from logging import getLogger  # noqa: E402

logger = getLogger(__name__)

# ======================
# Parameters
# ======================
WEIGHT_PATH = "fast-depth.onnx"
MODEL_PATH = "fast-depth.onnx.prototxt"
REMOTE_PATH = "https://storage.googleapis.com/ailia-models/fast-depth/"
SOURCE_IMAGE_PATH = "data"
SAVE_IMAGE_PATH = "img"
IMAGE_PATH = "data/img/00001.png"
DEPTH_MIN = 0  # In meters.
DEPTH_MAX = 5  # In meters.
OUTPUT_SIZE = (224, 224)

# ======================
# Argument Parser Config
# ======================
parser = get_base_parser("FastDepth", SOURCE_IMAGE_PATH, SAVE_IMAGE_PATH)
parser.add_argument(
    "--savepath",
    default="img",
    type=str,
    metavar="PATH",
    help="Path to output directory",
)
parser.add_argument(
    "--use_fixed_scale",
    action="store_true",
    help="Use fixed range of depth for color scale."
)

args = update_parser(parser)


# ======================
# Main functions
# ======================
def _make_dataset(img):
    input_np, _ = val_transform(img, None, OUTPUT_SIZE)
    input_tensor = input_np.transpose((2, 0, 1)).copy()
    while input_tensor.ndim < 3:
        input_tensor = np.expand_dims(input_tensor, 0)
    return [np.expand_dims(input_tensor, 0)]


def _prepare_data(args, frame=None):
    if args.video is not None:
        return _make_dataset(frame)
    else:
        path = os.path.join(".", IMAGE_PATH)
        with Image.open(path) as im:
            rgb = np.asarray(im)
        return _make_dataset(rgb)


def _initialize_net(args):
    return ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=args.env_id)


def _infer(img, net):
    return net.predict(img)


def _estimate(img, model, args):
    img_depth = _infer(img, model)
    depth_pred = np.squeeze(img_depth)
    if args.use_fixed_scale:
        scale_min = min(DEPTH_MIN, np.min(depth_pred))
        scale_max = max(DEPTH_MAX, np.max(depth_pred))
    else:
        scale_min = np.min(depth_pred)
        scale_max = np.max(depth_pred)
    depth_pred_col = utils_misc.colored_depthmap(
        depth_pred,
        scale_min,
        scale_max,
    )

    return depth_pred_col


def recognize_from_image():
    # Prepare input data.
    dataset = _prepare_data(args)

    # Initialize net.
    net = _initialize_net(args)

    # Inference
    logger.info("Start inference...")
    if args.benchmark:
        logger.info("BENCHMARK mode")
        for i in range(5):
            start = int(round(time.time() * 1000))
            _estimate(dataset[0], net, args)
            end = int(round(time.time() * 1000))
            logger.info(f"\tailia processing time {end - start} ms")
    else:
        depth_pred_col = _estimate(dataset[0], net, args)
        stem = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
        filepath = os.path.join(args.savepath, f"{stem}_depth.png")
        utils_misc.save_image(depth_pred_col, filepath)
    logger.info("Script finished successfully.")


def recognize_from_video():
    # Initialize net.
    net = _initialize_net(args)

    capture = get_capture(args.video)

    while True:
        ret, frame = capture.read()
        if (cv2.waitKey(1) & 0xFF == ord("q")) or not ret:
            break

        # Prepare input data.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cut_max_square(frame)
        dataset = _prepare_data(args, frame)

        # Inference
        depth_pred_col = _estimate(dataset[0], net, args)

        # Postprocessing
        cv2.imshow(
            "frame", cv2.cvtColor(depth_pred_col.astype("uint8"), cv2.COLOR_RGB2BGR)
        )

    capture.release()
    cv2.destroyAllWindows()
    logger.info("Script finished successfully.")


def main():
    # Check model files and download.
    check_and_download_models(
        WEIGHT_PATH,
        MODEL_PATH,
        REMOTE_PATH,
    )

    if args.video is not None:
        # Video mode
        recognize_from_video()
    else:
        # Image mode
        recognize_from_image()


if __name__ == "__main__":
    main()
