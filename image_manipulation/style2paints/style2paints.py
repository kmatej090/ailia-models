import sys, os
import time
import argparse
import json

import numpy as np
import cv2

import ailia

# import original modules
sys.path.append('../../util')
from utils import get_base_parser, update_parser  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
from detector_utils import load_image  # noqa: E402C

from style2paints_utils import *

# ======================
# Parameters
# ======================

WEIGHT_HEAD_PATH = 'head.onnx'
WEIGHT_NECK_PATH = 'neck.onnx'
WEIGHT_BABY_PATH = 'baby.onnx'
WEIGHT_TAIL_PATH = 'tail.onnx'
WEIGHT_GIRD_PATH = 'gird.onnx'
MODEL_HEAD_PATH = 'head.onnx.prototxt'
MODEL_NECK_PATH = 'neck.onnx.prototxt'
MODEL_BABY_PATH = 'baby.onnx.prototxt'
MODEL_TAIL_PATH = 'tail.onnx.prototxt'
MODEL_GIRD_PATH = 'gird.onnx.prototxt'
REMOTE_PATH = \
    'https://storage.googleapis.com/ailia-models/style2paints/'

IMAGE_PATH = 'Apr19H22M03S00R696.jpg'
SAVE_IMAGE_PATH = 'output.png'

# ======================
# Arguemnt Parser Config
# ======================

parser = get_base_parser(
    'Style2Paints model', IMAGE_PATH, SAVE_IMAGE_PATH
)
parser.add_argument(
    '--onnx',
    action='store_true',
    help='execute onnxruntime version.'
)
args = update_parser(parser)



# ======================
# Secondaty Functions
# ======================


def preprocess(img, de_painting=None):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_1024 = k_resize(img, 64)

    if de_painting is not None:
        vice_sketch_1024 = cv2.cvtColor(de_painting, cv2.COLOR_BGR2GRAY)
        vice_sketch_1024 = k_resize(vice_sketch_1024, 64)
        img_256 = mini_norm(k_resize(min_k_down(vice_sketch_1024, 2), 16))
        img_128 = hard_norm(sk_resize(min_k_down(vice_sketch_1024, 4), 32))
    else:
        img_256 = mini_norm(k_resize(min_k_down(img_1024, 2), 16))
        img_128 = hard_norm(sk_resize(min_k_down(img_1024, 4), 32))
    # cv2.imwrite('./sketch.128.jpg', img_128)
    # cv2.imwrite('./sketch.256.jpg', img_256)

    return img_1024.astype(np.float32), img_256.astype(np.float32), img_128.astype(np.float32)


def go_head(net_head, sketch, global_hint, local_hint, global_hint_x, alpha=1.0):
    ip1 = sketch[None, :, :, None]
    ip3 = global_hint[None, :, :, :]
    ip4 = local_hint[None, :, :, :]
    ip3x = global_hint_x[None, :, :, :]
    ipa = np.array([alpha], dtype=np.float32)[None, :]
    if not args.onnx:
        idx_ip1 = net_head.find_blob_index_by_name('import/Placeholder_1:0')
        idx_ip3 = net_head.find_blob_index_by_name('import/Placeholder_2:0')
        idx_ip4 = net_head.find_blob_index_by_name('import/Placeholder_3:0')
        idx_ip3x = net_head.find_blob_index_by_name('import/Placeholder_4:0')
        idx_ipa = net_head.find_blob_index_by_name('import/Placeholder:0')
        net_head.set_input_blob_shape(ip1.shape, idx_ip1)
        net_head.set_input_blob_shape(ip3.shape, idx_ip3)
        net_head.set_input_blob_shape(ip4.shape, idx_ip4)
        net_head.set_input_blob_shape(ip3x.shape, idx_ip3x)
        net_head.set_input_blob_shape(ipa.shape, idx_ipa)
        output = net_head.predict({
            'import/Placeholder_1:0': ip1,
            'import/Placeholder_2:0': ip3,
            'import/Placeholder_3:0': ip4,
            'import/Placeholder_4:0': ip3x,
            'import/Placeholder:0': ipa,
        })[0]
    else:
        in_ip3x = net_head.get_inputs()[0].name
        in_ip4 = net_head.get_inputs()[1].name
        in_ip3 = net_head.get_inputs()[2].name
        in_ip1 = net_head.get_inputs()[3].name
        in_ipa = net_head.get_inputs()[4].name
        out_head = net_head.get_outputs()[0].name
        output = net_head.run(
            [out_head],
            {in_ip1: ip1, in_ip3: ip3, in_ip4: ip4, in_ip3x: ip3x, in_ipa: ipa}
        )[0]

    head_op = output[0].clip(0, 255).astype(np.uint8)
    return head_op


def go_neck(net_neck, sketch, global_hint, local_hint, global_hint_x, alpha=1.0):
    ip1 = sketch[None, :, :, None]
    ip3 = global_hint[None, :, :, :]
    ip4 = local_hint[None, :, :, :]
    ip3x = global_hint_x[None, :, :, :]
    ipa = np.array([alpha], dtype=np.float32)[None, :]
    if not args.onnx:
        idx_ip1 = net_neck.find_blob_index_by_name('import/Placeholder_1:0')
        idx_ip3 = net_neck.find_blob_index_by_name('import/Placeholder_2:0')
        idx_ip4 = net_neck.find_blob_index_by_name('import/Placeholder_3:0')
        idx_ip3x = net_neck.find_blob_index_by_name('import/Placeholder_4:0')
        idx_ipa = net_neck.find_blob_index_by_name('import/Placeholder:0')
        net_neck.set_input_blob_shape(ip1.shape, idx_ip1)
        net_neck.set_input_blob_shape(ip3.shape, idx_ip3)
        net_neck.set_input_blob_shape(ip4.shape, idx_ip4)
        net_neck.set_input_blob_shape(ip3x.shape, idx_ip3x)
        net_neck.set_input_blob_shape(ipa.shape, idx_ipa)
        output = net_neck.predict({
            'import/Placeholder_1:0': ip1,
            'import/Placeholder_2:0': ip3,
            'import/Placeholder_3:0': ip4,
            'import/Placeholder_4:0': ip3x,
            'import/Placeholder:0': ipa,
        })[0]
    else:
        in_ip3x = net_neck.get_inputs()[0].name
        in_ip4 = net_neck.get_inputs()[1].name
        in_ip3 = net_neck.get_inputs()[2].name
        in_ip1 = net_neck.get_inputs()[3].name
        in_ipa = net_neck.get_inputs()[4].name
        out_neck = net_neck.get_outputs()[0].name
        output = net_neck.run(
            [out_neck],
            {in_ip1: ip1, in_ip3: ip3, in_ip4: ip4, in_ip3x: ip3x, in_ipa: ipa}
        )[0]

    neck_op = output[0].clip(0, 255).astype(np.uint8)
    return neck_op


def go_gird(net_gird, sketch, latent, hint):
    ip1 = sketch[None, :, :, None]
    ip3 = latent[None, :, :, :]
    ip4 = hint[None, :, :, :]
    if not args.onnx:
        idx_ip1 = net_gird.find_blob_index_by_name('import/Placeholder_1:0')
        idx_ip3 = net_gird.find_blob_index_by_name('import/Placeholder_2:0')
        idx_ip4 = net_gird.find_blob_index_by_name('import/Placeholder_3:0')
        net_gird.set_input_blob_shape(ip1.shape, idx_ip1)
        net_gird.set_input_blob_shape(ip3.shape, idx_ip3)
        net_gird.set_input_blob_shape(ip4.shape, idx_ip4)
        output = net_gird.predict({
            'import/Placeholder_1:0': ip1,
            'import/Placeholder_2:0': ip3,
            'import/Placeholder_3:0': ip4,
        })[0]
    else:
        in_ip4 = net_gird.get_inputs()[0].name
        in_ip3 = net_gird.get_inputs()[1].name
        in_ip1 = net_gird.get_inputs()[2].name
        out_gird = net_gird.get_outputs()[0].name
        output = net_gird.run([out_gird],
                              {in_ip1: ip1, in_ip3: ip3, in_ip4: ip4})[0]

    gird_op = output[0].clip(0, 255).astype(np.uint8)
    return gird_op


def go_tail(net_tail, x):
    x = x[None, :, :, :].astype(np.float32)
    if not args.onnx:
        net_tail.set_input_shape(x.shape)
        output = net_tail.predict({
            'import/Placeholder_857:0': x,
        })[0]
    else:
        in_ip3B = net_tail.get_inputs()[0].name
        out_tail = net_tail.get_outputs()[0].name
        output = net_tail.run([out_tail],
                              {in_ip3B: x})[0]

    tail_op = output[0].clip(0, 255).astype(np.uint8)
    return tail_op


def go_baby(net_baby, sketch, local_hint):
    ip1 = sketch[None, :, :, None]
    ip4 = local_hint[None, :, :, :]
    if not args.onnx:
        idx_ip1 = net_baby.find_blob_index_by_name('import/Placeholder_1:0')
        idx_ip4 = net_baby.find_blob_index_by_name('import/Placeholder_3:0')
        net_baby.set_input_blob_shape(ip1.shape, idx_ip1)
        net_baby.set_input_blob_shape(ip4.shape, idx_ip4)
        output = net_baby.predict({
            'import/Placeholder_1:0': ip1,
            'import/Placeholder_3:0': ip4,
        })[0]
    else:
        in_ip4 = net_baby.get_inputs()[0].name
        in_ip1 = net_baby.get_inputs()[1].name
        out_gird = net_baby.get_outputs()[0].name
        output = net_baby.run([out_gird],
                              {in_ip4: ip4, in_ip1: ip1})[0]

    baby_op = output[0].clip(0, 255).astype(np.uint8)
    return baby_op


# ======================
# Main functions
# ======================


def predict(img, dict_net, options):
    points = options["points"]
    method = options["method"]
    alpha = options["alpha"]
    reference = options["reference"]
    lineColor = options["lineColor"]
    line = options["line"]

    img = min_resize(img, 512)
    img = cv_denoise(img)
    img = sensitive(img, s=5.0)
    img = go_tail(dict_net['tail'], img)
    cv2.imwrite('./sketch.improved.jpg', img)
    img = cv2.imread('./sketch.improved.jpg')

    std = cal_std(img)
    print('std = ' + str(std))
    need_de_painting = (std > 100.0) and method == 'rendering'
    img2 = None
    if method == 'recolorization' or need_de_painting:
        img2 = go_passline(img)
        img2 = min_k_down_c(img2, 2)
        img2 = cv_denoise(img2)
        img2 = go_tail(dict_net['tail'], img2)
        img2 = sensitive(img2, s=5.0)
        img2 = min_black(img2)

    de_painting = None
    if method == 'colorization':
        img = min_black(img)
        cv2.imwrite('sketch.colorization.jpg', img)
    elif method == 'rendering':
        img = eye_black(img)
        cv2.imwrite('sketch.rendering.jpg', img)
        if need_de_painting:
            de_painting = img2
            cv2.imwrite('de_painting.jpg', de_painting)
    elif method == 'recolorization':
        img = img2
        cv2.imwrite('sketch.recolorization.jpg', img)

    img_1024, img_256, img_128 = preprocess(img, de_painting)
    print('sketch prepared')

    x = np.zeros(shape=(img_128.shape[0], img_128.shape[1], 4), dtype=np.float32)
    x = opreate_normal_hint(x, points, type=0, length=1)
    baby = go_baby(dict_net['baby'], img_128, x)
    baby = de_line(baby, img_128)
    for _ in range(16):
        baby = blur_line(baby, img_128)

    baby = go_tail(dict_net['tail'], baby)
    baby = clip_15(baby)
    print('baby born')

    latent = d_resize(baby, img_256.shape).astype(np.float32)
    hint = ini_hint(img_256)
    composition = go_gird(dict_net['gird'], img_256, latent, hint)
    if line:
        composition = emph_line(
            composition,
            d_resize(min_k_down(img_1024, 2), composition.shape),
            lineColor
        )
    composition = go_tail(dict_net['tail'], composition)
    cv2.imwrite('composition.jpg', composition)
    print('composition saved')

    global_hint = k_resize(composition, 14).astype(np.float32)
    local_hint = opreate_normal_hint(ini_hint(img_1024), points, type=2, length=2)
    global_hint_x = (
        k_resize(reference, 14) if reference is not None else k_resize(composition, 14)
    ).astype(np.float32)

    print('method: ' + method)
    if method == 'rendering':
        result = go_neck(
            dict_net['neck'], img_1024, global_hint, local_hint, global_hint_x,
            alpha=(1 - alpha) if reference is not None else 1)
    else:
        result = go_head(
            dict_net['head'], img_1024, global_hint, local_hint, global_hint_x,
            alpha=(1 - alpha) if reference is not None else 1)

    result = go_tail(dict_net['tail'], result)

    return result


def recognize_from_image(filename, dict_net):
    # prepare input data
    img = load_image(filename)
    print(f'input image shape: {img.shape}')

    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    json_file = '.'.join([filename.rsplit('.', 1)[0], 'json'])
    if not os.path.exists(json_file):
        raise FileNotFoundError('%s not exists' % json_file)

    with open(json_file) as f:
        options = json.load(f)

    points = options["points"]
    for _ in range(len(points)):
        points[_][1] = 1 - points[_][1]
    options["method"] = options.get("method", "colorization")
    options["alpha"] = float(options.get("alpha", 0.0))
    if options.get("hasReference", False):
        ref_file = options.get("reference", "style.jpg")
        if not os.path.exists(ref_file):
            raise FileNotFoundError('%s not exists' % ref_file)
        reference = cv2.imread(ref_file)
        scale = max(reference.shape[:2]) / 256
        if scale > 1.0:
            reference = cv2.resize(
                reference, (int(reference.shape[1] / scale), int(reference.shape[0] / scale))
            )
        options["reference"] = s_enhance(reference)
    else:
        options["reference"] = None
    options["line"] = options.get('line', False)
    options["lineColor"] = np.array(options.get('lineColor', [0, 0, 0]))

    # inference
    print('Start inference...')
    if args.benchmark:
        print('BENCHMARK mode')
        for i in range(5):
            start = int(round(time.time() * 1000))
            result = predict(img, dict_net, options)
            end = int(round(time.time() * 1000))
            print(f'\tailia processing time {end - start} ms')
    else:
        result = predict(img, dict_net, options)

    # plot result
    cv2.imwrite(args.savepath, result)
    print('Script finished successfully.')


def main():
    # model files check and download
    print('=== head model ===')
    check_and_download_models(WEIGHT_HEAD_PATH, MODEL_HEAD_PATH, REMOTE_PATH)
    print('=== neck model ===')
    check_and_download_models(WEIGHT_NECK_PATH, MODEL_NECK_PATH, REMOTE_PATH)
    print('=== baby model ===')
    check_and_download_models(WEIGHT_BABY_PATH, MODEL_BABY_PATH, REMOTE_PATH)
    print('=== tail model ===')
    check_and_download_models(WEIGHT_TAIL_PATH, MODEL_TAIL_PATH, REMOTE_PATH)
    print('=== gird model ===')
    check_and_download_models(WEIGHT_GIRD_PATH, MODEL_GIRD_PATH, REMOTE_PATH)

    # load model
    env_id = args.env_id
    print(f'env_id: {env_id}')

    # initialize
    if not args.onnx:
        net_head = ailia.Net(MODEL_HEAD_PATH, WEIGHT_HEAD_PATH, env_id=env_id)
        net_neck = ailia.Net(MODEL_NECK_PATH, WEIGHT_NECK_PATH, env_id=env_id)
        net_baby = ailia.Net(MODEL_BABY_PATH, WEIGHT_BABY_PATH, env_id=env_id)
        net_tail = ailia.Net(MODEL_TAIL_PATH, WEIGHT_TAIL_PATH, env_id=env_id)
        net_gird = ailia.Net(MODEL_GIRD_PATH, WEIGHT_GIRD_PATH, env_id=env_id)
    else:
        import onnxruntime
        net_head = onnxruntime.InferenceSession(WEIGHT_HEAD_PATH)
        net_neck = onnxruntime.InferenceSession(WEIGHT_NECK_PATH)
        net_baby = onnxruntime.InferenceSession(WEIGHT_BABY_PATH)
        net_tail = onnxruntime.InferenceSession(WEIGHT_TAIL_PATH)
        net_gird = onnxruntime.InferenceSession(WEIGHT_GIRD_PATH)
    dict_net = {
        "head": net_head,
        "neck": net_neck,
        "baby": net_baby,
        "tail": net_tail,
        "gird": net_gird,
    }

    recognize_from_image(args.input, dict_net)


if __name__ == '__main__':
    main()
