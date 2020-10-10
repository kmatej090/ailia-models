import os
import sys
import time
import argparse
import re
from collections import deque

import numpy as np
import cv2

import ailia

# import original modules
sys.path.append('../../util')
sys.path.append('util')
from utils import check_file_existance  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
from webcamera_utils import get_capture  # noqa: E402C

from st_gcn_util import naive_pose_tracker, render_video

# ======================
# Parameters
# ======================
WEIGHT_PATH = 'st_gcn.onnx'
MODEL_PATH = 'st_gcn.onnx.prototxt'
REMOTE_PATH = 'https://storage.googleapis.com/ailia-models/st_gcn/'

MODEL_POSE_PATH = 'pose_deploy.prototxt'
# MODEL_POSE_PATH = 'pose_deploy_linevec.prototxt'
WEIGHT_POSE_PATH = 'pose_iter_440000.caffemodel'
REMOTE_POSE_PATH = 'http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/'

POSE_ALGORITHM_OPEN_POSE_SINGLE_SCALE = (12)
POSE_ALGORITHM = ailia.POSE_ALGORITHM_OPEN_POSE
# POSE_ALGORITHM = POSE_ALGORITHM_OPEN_POSE_SINGLE_SCALE

IMAGE_PATH = 'skateboarding.mp4'
# IMAGE_HEIGHT = 112
# IMAGE_WIDTH = 112
# DURATION = 16

KINETICS_LABEL = [
    'abseiling',
    'air drumming',
    'answering questions',
    'applauding',
    'applying cream',
    'archery',
    'arm wrestling',
    'arranging flowers',
    'assembling computer',
    'auctioning',
    'baby waking up',
    'baking cookies',
    'balloon blowing',
    'bandaging',
    'barbequing',
    'bartending',
    'beatboxing',
    'bee keeping',
    'belly dancing',
    'bench pressing',
    'bending back',
    'bending metal',
    'biking through snow',
    'blasting sand',
    'blowing glass',
    'blowing leaves',
    'blowing nose',
    'blowing out candles',
    'bobsledding',
    'bookbinding',
    'bouncing on trampoline',
    'bowling',
    'braiding hair',
    'breading or breadcrumbing',
    'breakdancing',
    'brush painting',
    'brushing hair',
    'brushing teeth',
    'building cabinet',
    'building shed',
    'bungee jumping',
    'busking',
    'canoeing or kayaking',
    'capoeira',
    'carrying baby',
    'cartwheeling',
    'carving pumpkin',
    'catching fish',
    'catching or throwing baseball',
    'catching or throwing frisbee',
    'catching or throwing softball',
    'celebrating',
    'changing oil',
    'changing wheel',
    'checking tires',
    'cheerleading',
    'chopping wood',
    'clapping',
    'clay pottery making',
    'clean and jerk',
    'cleaning floor',
    'cleaning gutters',
    'cleaning pool',
    'cleaning shoes',
    'cleaning toilet',
    'cleaning windows',
    'climbing a rope',
    'climbing ladder',
    'climbing tree',
    'contact juggling',
    'cooking chicken',
    'cooking egg',
    'cooking on campfire',
    'cooking sausages',
    'counting money',
    'country line dancing',
    'cracking neck',
    'crawling baby',
    'crossing river',
    'crying',
    'curling hair',
    'cutting nails',
    'cutting pineapple',
    'cutting watermelon',
    'dancing ballet',
    'dancing charleston',
    'dancing gangnam style',
    'dancing macarena',
    'deadlifting',
    'decorating the christmas tree',
    'digging',
    'dining',
    'disc golfing',
    'diving cliff',
    'dodgeball',
    'doing aerobics',
    'doing laundry',
    'doing nails',
    'drawing',
    'dribbling basketball',
    'drinking',
    'drinking beer',
    'drinking shots',
    'driving car',
    'driving tractor',
    'drop kicking',
    'drumming fingers',
    'dunking basketball',
    'dying hair',
    'eating burger',
    'eating cake',
    'eating carrots',
    'eating chips',
    'eating doughnuts',
    'eating hotdog',
    'eating ice cream',
    'eating spaghetti',
    'eating watermelon',
    'egg hunting',
    'exercising arm',
    'exercising with an exercise ball',
    'extinguishing fire',
    'faceplanting',
    'feeding birds',
    'feeding fish',
    'feeding goats',
    'filling eyebrows',
    'finger snapping',
    'fixing hair',
    'flipping pancake',
    'flying kite',
    'folding clothes',
    'folding napkins',
    'folding paper',
    'front raises',
    'frying vegetables',
    'garbage collecting',
    'gargling',
    'getting a haircut',
    'getting a tattoo',
    'giving or receiving award',
    'golf chipping',
    'golf driving',
    'golf putting',
    'grinding meat',
    'grooming dog',
    'grooming horse',
    'gymnastics tumbling',
    'hammer throw',
    'headbanging',
    'headbutting',
    'high jump',
    'high kick',
    'hitting baseball',
    'hockey stop',
    'holding snake',
    'hopscotch',
    'hoverboarding',
    'hugging',
    'hula hooping',
    'hurdling',
    'hurling (sport)',
    'ice climbing',
    'ice fishing',
    'ice skating',
    'ironing',
    'javelin throw',
    'jetskiing',
    'jogging',
    'juggling balls',
    'juggling fire',
    'juggling soccer ball',
    'jumping into pool',
    'jumpstyle dancing',
    'kicking field goal',
    'kicking soccer ball',
    'kissing',
    'kitesurfing',
    'knitting',
    'krumping',
    'laughing',
    'laying bricks',
    'long jump',
    'lunge',
    'making a cake',
    'making a sandwich',
    'making bed',
    'making jewelry',
    'making pizza',
    'making snowman',
    'making sushi',
    'making tea',
    'marching',
    'massaging back',
    'massaging feet',
    'massaging legs', "massaging person's head", 'milking cow',
    'mopping floor',
    'motorcycling',
    'moving furniture',
    'mowing lawn',
    'news anchoring',
    'opening bottle',
    'opening present',
    'paragliding',
    'parasailing',
    'parkour',
    'passing American football (in game)',
    'passing American football (not in game)',
    'peeling apples',
    'peeling potatoes',
    'petting animal (not cat)',
    'petting cat',
    'picking fruit',
    'planting trees',
    'plastering',
    'playing accordion',
    'playing badminton',
    'playing bagpipes',
    'playing basketball',
    'playing bass guitar',
    'playing cards',
    'playing cello',
    'playing chess',
    'playing clarinet',
    'playing controller',
    'playing cricket',
    'playing cymbals',
    'playing didgeridoo',
    'playing drums',
    'playing flute',
    'playing guitar',
    'playing harmonica',
    'playing harp',
    'playing ice hockey',
    'playing keyboard',
    'playing kickball',
    'playing monopoly',
    'playing organ',
    'playing paintball',
    'playing piano',
    'playing poker',
    'playing recorder',
    'playing saxophone',
    'playing squash or racquetball',
    'playing tennis',
    'playing trombone',
    'playing trumpet',
    'playing ukulele',
    'playing violin',
    'playing volleyball',
    'playing xylophone',
    'pole vault',
    'presenting weather forecast',
    'pull ups',
    'pumping fist',
    'pumping gas',
    'punching bag',
    'punching person (boxing)',
    'push up',
    'pushing car',
    'pushing cart',
    'pushing wheelchair',
    'reading book',
    'reading newspaper',
    'recording music',
    'riding a bike',
    'riding camel',
    'riding elephant',
    'riding mechanical bull',
    'riding mountain bike',
    'riding mule',
    'riding or walking with horse',
    'riding scooter',
    'riding unicycle',
    'ripping paper',
    'robot dancing',
    'rock climbing',
    'rock scissors paper',
    'roller skating',
    'running on treadmill',
    'sailing',
    'salsa dancing',
    'sanding floor',
    'scrambling eggs',
    'scuba diving',
    'setting table',
    'shaking hands',
    'shaking head',
    'sharpening knives',
    'sharpening pencil',
    'shaving head',
    'shaving legs',
    'shearing sheep',
    'shining shoes',
    'shooting basketball',
    'shooting goal (soccer)',
    'shot put',
    'shoveling snow',
    'shredding paper',
    'shuffling cards',
    'side kick',
    'sign language interpreting',
    'singing',
    'situp',
    'skateboarding',
    'ski jumping',
    'skiing (not slalom or crosscountry)',
    'skiing crosscountry',
    'skiing slalom',
    'skipping rope',
    'skydiving',
    'slacklining',
    'slapping',
    'sled dog racing',
    'smoking',
    'smoking hookah',
    'snatch weight lifting',
    'sneezing',
    'sniffing',
    'snorkeling',
    'snowboarding',
    'snowkiting',
    'snowmobiling',
    'somersaulting',
    'spinning poi',
    'spray painting',
    'spraying',
    'springboard diving',
    'squat',
    'sticking tongue out',
    'stomping grapes',
    'stretching arm',
    'stretching leg',
    'strumming guitar',
    'surfing crowd',
    'surfing water',
    'sweeping floor',
    'swimming backstroke',
    'swimming breast stroke',
    'swimming butterfly stroke',
    'swing dancing',
    'swinging legs',
    'swinging on something',
    'sword fighting',
    'tai chi',
    'taking a shower',
    'tango dancing',
    'tap dancing',
    'tapping guitar',
    'tapping pen',
    'tasting beer',
    'tasting food',
    'testifying',
    'texting',
    'throwing axe',
    'throwing ball',
    'throwing discus',
    'tickling',
    'tobogganing',
    'tossing coin',
    'tossing salad',
    'training dog',
    'trapezing',
    'trimming or shaving beard',
    'trimming trees',
    'triple jump',
    'tying bow tie',
    'tying knot (not on a tie)',
    'tying tie',
    'unboxing',
    'unloading truck',
    'using computer',
    'using remote controller (not gaming)',
    'using segway',
    'vault',
    'waiting in line',
    'walking the dog',
    'washing dishes',
    'washing feet',
    'washing hair',
    'washing hands',
    'water skiing',
    'water sliding',
    'watering plants',
    'waxing back',
    'waxing chest',
    'waxing eyebrows',
    'waxing legs',
    'weaving basket',
    'welding',
    'whistling',
    'windsurfing',
    'wrapping present',
    'wrestling',
    'writing',
    'yawning',
    'yoga',
    'zumba'
]

# ======================
# Arguemnt Parser Config
# ======================
parser = argparse.ArgumentParser(
    description='ST-GCN model'
)
parser.add_argument(
    '-i', '--input', metavar='IMAGE',
    default=IMAGE_PATH,
    help='The input image path.'
)
parser.add_argument(
    '-v', '--video', metavar='VIDEO',
    default=None,
    help='The input video path. ' +
         'If the VIDEO argument is set to 0, the webcam input will be used.'
)
parser.add_argument(
    '-b', '--benchmark',
    action='store_true',
    help='Running the inference on the same input 5 times ' +
         'to measure execution performance. (Cannot be used in video mode)'
)
# parser.add_argument(
#     '-d', '--duration', metavar='DURATION',
#     default=DURATION,
#     help='Sampling duration.',
#     type=int
# )
args = parser.parse_args()


# ======================
# Secondaty Functions
# ======================
def pose_postprocess(pose_keypoints):
    pose_keypoints[:, :, 0:2] = pose_keypoints[:, :, 0:2] - 0.5
    pose_keypoints[:, :, 0][pose_keypoints[:, :, 2] == 0] = 0
    pose_keypoints[:, :, 1][pose_keypoints[:, :, 2] == 0] = 0
    return pose_keypoints


def postprocess(output, feature, num_person):
    intensity = (feature * feature).sum(axis=0) ** 0.5

    # get result
    # classification result of the full sequence
    voting_label = output.sum(axis=3). \
        sum(axis=2).sum(axis=1).argmax(axis=0)
    voting_label_name = KINETICS_LABEL[voting_label]
    # classification result for each person of the latest frame
    latest_frame_label = [
        output[:, :, :, m].sum(axis=2)[:, -1].argmax(axis=0) for m in range(num_person)
    ]
    latest_frame_label_name = [KINETICS_LABEL[l]
                               for l in latest_frame_label]

    _, num_frame, _, num_person = output.shape
    video_label_name = list()
    for t in range(num_frame):
        frame_label_name = list()
        for m in range(num_person):
            person_label = output[:, t, :, m].sum(axis=1).argmax(axis=0)
            person_label_name = KINETICS_LABEL[person_label]
            frame_label_name.append(person_label_name)
        video_label_name.append(frame_label_name)

    return voting_label_name, video_label_name, output, intensity


def hsv_to_rgb(h, s, v):
    bgr = cv2.cvtColor(
        np.array([[[h, s, v]]], dtype=np.uint8), cv2.COLOR_HSV2BGR
    )[0][0]
    return (int(bgr[2]), int(bgr[1]), int(bgr[0]))


def line(input_img, person, point1, point2):
    threshold = 0.2
    if person.points[point1].score > threshold and \
            person.points[point2].score > threshold:
        color = hsv_to_rgb(255 * point1 / ailia.POSE_KEYPOINT_CNT, 255, 255)

        x1 = int(input_img.shape[1] * person.points[point1].x)
        y1 = int(input_img.shape[0] * person.points[point1].y)
        x2 = int(input_img.shape[1] * person.points[point2].x)
        y2 = int(input_img.shape[0] * person.points[point2].y)
        cv2.line(input_img, (x1, y1), (x2, y2), color, 5)


def display_result(input_img, pose):
    count = pose.get_object_count()
    for idx in range(count):
        person = pose.get_object_pose(idx)

        line(input_img, person, ailia.POSE_KEYPOINT_NOSE,
             ailia.POSE_KEYPOINT_SHOULDER_CENTER)
        line(input_img, person, ailia.POSE_KEYPOINT_SHOULDER_LEFT,
             ailia.POSE_KEYPOINT_SHOULDER_CENTER)
        line(input_img, person, ailia.POSE_KEYPOINT_SHOULDER_RIGHT,
             ailia.POSE_KEYPOINT_SHOULDER_CENTER)

        line(input_img, person, ailia.POSE_KEYPOINT_EYE_LEFT,
             ailia.POSE_KEYPOINT_NOSE)
        line(input_img, person, ailia.POSE_KEYPOINT_EYE_RIGHT,
             ailia.POSE_KEYPOINT_NOSE)
        line(input_img, person, ailia.POSE_KEYPOINT_EAR_LEFT,
             ailia.POSE_KEYPOINT_EYE_LEFT)
        line(input_img, person, ailia.POSE_KEYPOINT_EAR_RIGHT,
             ailia.POSE_KEYPOINT_EYE_RIGHT)

        line(input_img, person, ailia.POSE_KEYPOINT_ELBOW_LEFT,
             ailia.POSE_KEYPOINT_SHOULDER_LEFT)
        line(input_img, person, ailia.POSE_KEYPOINT_ELBOW_RIGHT,
             ailia.POSE_KEYPOINT_SHOULDER_RIGHT)
        line(input_img, person, ailia.POSE_KEYPOINT_WRIST_LEFT,
             ailia.POSE_KEYPOINT_ELBOW_LEFT)
        line(input_img, person, ailia.POSE_KEYPOINT_WRIST_RIGHT,
             ailia.POSE_KEYPOINT_ELBOW_RIGHT)

        line(input_img, person, ailia.POSE_KEYPOINT_BODY_CENTER,
             ailia.POSE_KEYPOINT_SHOULDER_CENTER)
        line(input_img, person, ailia.POSE_KEYPOINT_HIP_LEFT,
             ailia.POSE_KEYPOINT_BODY_CENTER)
        line(input_img, person, ailia.POSE_KEYPOINT_HIP_RIGHT,
             ailia.POSE_KEYPOINT_BODY_CENTER)

        line(input_img, person, ailia.POSE_KEYPOINT_KNEE_LEFT,
             ailia.POSE_KEYPOINT_HIP_LEFT)
        line(input_img, person, ailia.POSE_KEYPOINT_ANKLE_LEFT,
             ailia.POSE_KEYPOINT_KNEE_LEFT)
        line(input_img, person, ailia.POSE_KEYPOINT_KNEE_RIGHT,
             ailia.POSE_KEYPOINT_HIP_RIGHT)
        line(input_img, person, ailia.POSE_KEYPOINT_ANKLE_RIGHT,
             ailia.POSE_KEYPOINT_KNEE_RIGHT)


# ======================
# Main functions
# ======================
def recognize_offline(input, pose, net):
    capture = cv2.VideoCapture(input)

    video_length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    pose_tracker = naive_pose_tracker(data_frame=video_length)

    # # initiate pyopenpose
    # sys.path.insert(0, '/usr/local/python')
    # sys.path.insert(0, '/usr/local/build/python')
    # from openpose import pyopenpose as op
    # opWrapper = op.WrapperPython()
    # params = dict(model_folder='./st-gcn/models', model_pose='COCO')
    # opWrapper.configure(params)
    # opWrapper.start()

    # pose estimation
    frame_index = 0
    frames = list()
    while True:
        ret, frame = capture.read()
        if frame is None:
            break

        source_H, source_W, _ = frame.shape
        img = cv2.resize(
            frame, (256 * source_W // source_H, 256))
        frames.append(img)
        H, W, _ = img.shape

        # pose estimate
        if 0:
            datum = op.Datum()
            datum.cvInputData = img
            opWrapper.emplaceAndPop([datum])
            pose_keypoints = datum.poseKeypoints  # (num_person, num_joint, 3)
            if len(pose_keypoints.shape) != 3:
                continue
            print(f'[{frame_index}] person_count={len(pose_keypoints)}')

            # normalization
            pose_keypoints[:, :, 0] = pose_keypoints[:, :, 0] / W
            pose_keypoints[:, :, 1] = pose_keypoints[:, :, 1] / H
        else:
            IMAGE_HEIGHT = 240
            IMAGE_WIDTH = 320
            # IMAGE_HEIGHT = 368
            # IMAGE_WIDTH = 368
            img = cv2.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
            pose.compute(img)
            count = pose.get_object_count()
            # display_result(img, pose)
            # cv2.imwrite("output/POSE-%08d.jpg" % frame_index, img)
            if count == 0:
                continue
            print(f'[{frame_index}] person_count={count}')

            pose_key = [
                ailia.POSE_KEYPOINT_NOSE,
                ailia.POSE_KEYPOINT_SHOULDER_CENTER,
                ailia.POSE_KEYPOINT_SHOULDER_RIGHT,
                ailia.POSE_KEYPOINT_ELBOW_RIGHT,
                ailia.POSE_KEYPOINT_WRIST_RIGHT,
                ailia.POSE_KEYPOINT_SHOULDER_LEFT,
                ailia.POSE_KEYPOINT_ELBOW_LEFT,
                ailia.POSE_KEYPOINT_WRIST_LEFT,
                ailia.POSE_KEYPOINT_HIP_RIGHT,
                ailia.POSE_KEYPOINT_KNEE_RIGHT,
                ailia.POSE_KEYPOINT_ANKLE_RIGHT,
                ailia.POSE_KEYPOINT_HIP_LEFT,
                ailia.POSE_KEYPOINT_KNEE_LEFT,
                ailia.POSE_KEYPOINT_ANKLE_LEFT,
                ailia.POSE_KEYPOINT_EYE_RIGHT,
                ailia.POSE_KEYPOINT_EYE_LEFT,
                ailia.POSE_KEYPOINT_EAR_RIGHT,
                ailia.POSE_KEYPOINT_EAR_LEFT,
            ]
            pose_keypoints = np.zeros((count, 18, 3))  # (num_person, num_joint, 3)
            for idx in range(count):
                person = pose.get_object_pose(idx)
                for i, key in enumerate(pose_key):
                    p = person.points[key]
                    pose_keypoints[idx, key, :] = [p.x, p.y, p.score]

        # for idx in range(len(pose_keypoints)):
        #     for i in range(18):
        #         print("{}: {}, {}, {}".format(i, pose_keypoints[idx,i,0], pose_keypoints[idx,i,1], pose_keypoints[idx,i,2]))

        pose_keypoints = pose_postprocess(pose_keypoints)

        pose_tracker.update(pose_keypoints, frame_index)
        frame_index += 1
        print('Pose estimation ({}/{}).'.format(frame_index, video_length))

    # frames = np.load('video.npy')
    # data = np.load('data.npy')
    data = pose_tracker.get_skeleton_sequence()

    # action recognition
    input_data = np.expand_dims(data, 0)
    print("data-------", input_data.shape)
    net.set_input_shape(input_data.shape)
    outputs = net.predict({
        'data': input_data
    })
    output, feature = outputs

    output = output[0]
    feature = feature[0]
    # classification result for each person of the latest frame
    _, _, _, num_person = data.shape
    voting_label_name, video_label_name, output, intensity = postprocess(output, feature, num_person)
    print("voting_label_name-------", voting_label_name)
    print("video_label_name-------", video_label_name)
    return data, voting_label_name, video_label_name, output, intensity, frames


def recognize_from_file(input, pose, net):
    # inferece
    print('Start inference...')
    if args.benchmark:
        print('BENCHMARK mode')
        for i in range(5):
            start = int(round(time.time() * 1000))
            result = recognize_offline(input, pose, net)
            end = int(round(time.time() * 1000))
            print(f'\tailia processing time {end - start} ms')
    else:
        result = recognize_offline(input, pose, net)

    print('Script finished successfully.')

    # render the video
    data, voting_label_name, video_label_name, output, intensity, frames = result
    images = render_video(
        data, voting_label_name,
        video_label_name, intensity, frames)

    # visualize
    for i, image in enumerate(images):
        image = image.astype(np.uint8)
        cv2.imshow("ST-GCN", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.imwrite("output/ST-GCN-%08d.jpg" % i, image)


def recognize_realtime(video, net):
    if video == '0':
        print('[INFO] Webcam mode is activated')
        capture = cv2.VideoCapture(0)
        if not capture.isOpened():
            print("[ERROR] webcamera not found")
            sys.exit(1)
    else:
        if check_file_existance(video):
            capture = cv2.VideoCapture(video)

    while True:
        ret, frame = capture.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if not ret:
            continue

        # show
        cv2.imshow('ST-GCN', frame)

    capture.release()
    cv2.destroyAllWindows()
    print('Script finished successfully.')


def main():
    # model files check and download
    check_and_download_models(WEIGHT_PATH, MODEL_PATH, REMOTE_PATH)
    check_and_download_models(WEIGHT_POSE_PATH, MODEL_POSE_PATH, REMOTE_POSE_PATH)

    # net initialize
    env_id = ailia.get_gpu_environment_id()
    print(f'env_id: {env_id}')
    net = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=env_id)

    pose = ailia.PoseEstimator(
        MODEL_POSE_PATH, WEIGHT_POSE_PATH, env_id=env_id, algorithm=POSE_ALGORITHM
    )
    pose.set_threshold(0.1)

    if args.video is not None:
        # video mode
        recognize_realtime(args.video, net)
    else:
        # image mode
        recognize_from_file(args.input, pose, net)


if __name__ == '__main__':
    main()
