#ailia detector api sample
import numpy as np
import time
import sys
import cv2

from modnet_utils import get_scale_factor

import ailia

# import original modules
sys.path.append('../../util')
from utils import get_base_parser, update_parser, get_savepath
from model_utils import check_and_download_models
import webcamera_utils

# logger
from logging import getLogger

logger = getLogger(__name__)

# ======================
# Arguemnt Parser Config
# ======================
IMAGE_PATH = 'input.jpg'
SAVE_IMAGE_PATH = 'output.jpg'

parser = get_base_parser('modnet model', IMAGE_PATH, SAVE_IMAGE_PATH)
parser.add_argument(
    '-c', '--composite',
    action='store_true',
    help='Composite input image and predicted alpha value'
)
args = update_parser(parser)
REMOTE_PATH = 'https://storage.googleapis.com/ailia-models/modnet/'

WEIGHT_PATH = "modnet.opt.onnx"
MODEL_PATH = "modnet.opt.onnx.prototxt"

HEIGHT = 512
WIDTH = 736

# ======================
# Main functions
# ======================
def recognize_from_image():
    env_id = args.env_id
    detector = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=env_id)

    # input image loop
    for image_path in args.input:
        # prepare input data
        logger.debug(f'input image: {image_path}')
        raw_img = cv2.imread(image_path)
        img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)
        img = (img - 127.5) / 127.5
        im_h, im_w, im_c = img.shape
        x, y = get_scale_factor(im_h, im_w, 512)
        img = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_AREA)

        img = np.transpose(img)
        img = np.swapaxes(img, 1, 2)
        img = np.expand_dims(img, axis=0).astype('float32')

        logger.debug(f'input image shape: {img.shape}')

        # inference
        logger.info('Start inference...')
        if args.benchmark:
            logger.info('BENCHMARK mode')
            for i in range(5):
                start = int(round(time.time() * 1000))
                pred = detector.predict(img)
                end = int(round(time.time() * 1000))
                logger.info(f'\tailia processing time {end - start} ms')
        else:
            pred = detector.predict(img)

        matte = (np.squeeze(pred[0]) * 255).astype('uint8')
        matte = cv2.resize(matte, dsize=(im_w, im_h), interpolation=cv2.INTER_AREA)

        if args.composite:
            img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2BGRA)
            img[:,:,3] = matte
            matte = img

        savepath = get_savepath(args.savepath, image_path)
        logger.info(f'saved at : {savepath}')
        cv2.imwrite(savepath, matte)

    logger.info('Script finished successfully.')


def recognize_from_video():
    # net initialize
    env_id = args.env_id
    detector = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=env_id)
    capture = webcamera_utils.get_capture(args.video)

    # create video writer if savepath is specified as video format
    if args.savepath != SAVE_IMAGE_PATH:
        logger.warning(
            'currently, video results cannot be output correctly...'
        )
        f_h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        f_w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        save_h, save_w = f_h, f_w
        writer = webcamera_utils.get_writer(args.savepath, save_h, save_w)
    else:
        writer = None

    while (True):
        ret, frame = capture.read()
        if (cv2.waitKey(1) & 0xFF == ord('q')) or not ret:
            break

        raw_img = frame
        img = (raw_img - 127.5) / 127.5
        im_h, im_w, im_c = img.shape
        x, y = get_scale_factor(im_h, im_w, 512)
        img = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_AREA)

        img = np.transpose(img)
        img = np.swapaxes(img, 1, 2)
        img = np.expand_dims(img, axis=0).astype('float32')

        pred = detector.predict(img)
        matte = (np.squeeze(pred[0]) * 255).astype('uint8')
        matte = cv2.resize(matte, dsize=(im_w, im_h), interpolation=cv2.INTER_AREA)

        cv2.imshow('frame', matte)

        # save results
        if writer is not None:
            writer.write(matte)

    capture.release()
    cv2.destroyAllWindows()
    if writer is not None:
        writer.release()
    logger.info('Script finished successfully.')


def main():
    # model files check and download
    check_and_download_models(WEIGHT_PATH, MODEL_PATH, REMOTE_PATH)

    if args.video is not None:
        # video mode
        recognize_from_video()
    else:
        # image mode
        recognize_from_image()


if __name__ == '__main__':
    main()
