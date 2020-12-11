import sys
import time
import json

import numpy as np
import cv2

import ailia

# import original modules
sys.path.append('../../util')
from utils import get_base_parser, update_parser  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
from detector_utils import load_image  # noqa: E402
from image_captioning_pytorch_utils import decode_sequence  # noqa: E402
import webcamera_utils  # noqa: E402


# ======================
# Parameters
# ======================
WEIGHT_CAPTIONING_FC_PATH = 'model_fc.onnx'
MODEL_CAPTIONING_FC_PATH = 'model_fc.onnx.prototxt'
WEIGHT_CAPTIONING_FC_RL_PATH = 'model_fc_rl.onnx'
MODEL_CAPTIONING_FC_RL_PATH = 'model_fc_rl.onnx.prototxt'
WEIGHT_CAPTIONING_FC_NSC_PATH = 'model_fc_nsc.onnx'
MODEL_CAPTIONING_FC_NSC_PATH = 'model_fc_nsc.onnx.prototxt'
WEIGHT_FEAT_PATH = 'model_feat.onnx'
MODEL_FEAT_PATH = 'model_feat.onnx.prototxt'
REMOTE_PATH = \
    'https://storage.googleapis.com/ailia-models/image_captioning_pytorch/'

IMAGE_PATH = 'demo.jpg'
SAVE_IMAGE_PATH = 'output.png'

VOCAB_FILE_PATH = 'vocab.json'

NORM_MEAN = [0.485, 0.456, 0.406]
NORM_STD = [0.229, 0.224, 0.225]

SLEEP_TIME = 0

INPUT_WIDTH = 640

# ======================
# Arguemnt Parser Config
# ======================
parser = get_base_parser(
    'ImageCaptioning.pytorch model', IMAGE_PATH, SAVE_IMAGE_PATH
)
parser.add_argument(
    '--model', type=str, default='fc',
    choices=('fc', 'fc_rl', 'fc_nsc'),
    help='captioning model (fc | fc_rl | fc_nsc)'
)
args = update_parser(parser)


# ======================
# Secondaty Functions
# ======================
def preprocess(img):
    h, w, _ = img.shape
    if w >= INPUT_WIDTH:
        img = cv2.resize(img, (INPUT_WIDTH, int(h*INPUT_WIDTH/w)))
    img = ((img / 255.0 - NORM_MEAN) / NORM_STD).astype(np.float32)
    img = img.transpose([2, 0, 1])
    return img


def post_processing(output):
    seq, _ = output

    with open(VOCAB_FILE_PATH) as f:
        vocab = json.loads(f.read())

    sents = decode_sequence(vocab, seq)

    return sents


# ======================
# Main functions
# ======================
def predict(img, net, my_resnet):
    # initial preprocesses
    h, w, _ = img.shape
    img = preprocess(img)

    # feedforward
    fc = my_resnet.predict({'img': img})[0]
    fc = np.expand_dims(fc, axis=0)
    output = net.predict({'fc_feats': fc})

    # post processes
    sents = post_processing(output)

    return sents


def recognize_from_image(filename, net, my_resnet):
    # prepare input data
    img = load_image(filename)
    print(f'input image shape: {img.shape}')

    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    # inference
    print('Start inference...')
    if args.benchmark:
        print('BENCHMARK mode')
        for i in range(5):
            start = int(round(time.time() * 1000))
            sents = predict(img, net, my_resnet)
            end = int(round(time.time() * 1000))
            print(f'\tailia processing time {end - start} ms')
    else:
        sents = predict(img, net, my_resnet)

    print('### Caption ### \n', sents[0], '\n')

    # plot result
    # cv2.imwrite(args.savepath, res_img)
    print('Script finished successfully.')


def recognize_from_video(video, net, my_resnet):
    capture = webcamera_utils.get_capture(video)

    # create video writer if savepath is specified as video format
    if args.savepath != SAVE_IMAGE_PATH:
        f_h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        f_w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        writer = webcamera_utils.get_writer(args.savepath, f_h, f_w)
    else:
        writer = None

    while (True):
        ret, frame = capture.read()
        if (cv2.waitKey(1) & 0xFF == ord('q')) or not ret:
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        sents = predict(img, net, my_resnet)

        print('Caption --->', sents[0])

        cv2.rectangle(
            frame, (0, 0), (frame.shape[1], 48), (255, 255, 255), thickness=-1
        )
        cv2.putText(
            frame,
            sents[0],
            (32, 32),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 0),
            2
        )

        cv2.imshow('frame', frame)
        time.sleep(SLEEP_TIME)

        # save results
        if writer is not None:
            writer.write(frame)

    capture.release()
    cv2.destroyAllWindows()
    if writer is not None:
        writer.release()
    print('Script finished successfully.')


def main():
    dic_model = {
        'fc': (WEIGHT_CAPTIONING_FC_PATH, MODEL_CAPTIONING_FC_PATH),
        'fc_rl': (WEIGHT_CAPTIONING_FC_RL_PATH, MODEL_CAPTIONING_FC_RL_PATH),
        'fc_nsc': (WEIGHT_CAPTIONING_FC_NSC_PATH, MODEL_CAPTIONING_FC_NSC_PATH),
    }
    weight_path, model_path = dic_model[args.model]

    # model files check and download
    print("=== Captioning model ===")
    check_and_download_models(weight_path, model_path, REMOTE_PATH)
    print("=== Feature model ===")
    check_and_download_models(WEIGHT_FEAT_PATH, MODEL_FEAT_PATH, REMOTE_PATH)

    # initialize
    net = ailia.Net(model_path, weight_path, env_id=args.env_id)
    my_resnet = ailia.Net(
        MODEL_FEAT_PATH, WEIGHT_FEAT_PATH, env_id=args.env_id
    )

    if args.video is not None:
        recognize_from_video(args.video, net, my_resnet)
    else:
        recognize_from_image(args.input, net, my_resnet)


if __name__ == '__main__':
    main()
