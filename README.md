# ailia-models

The collection of pre-trained, state-of-the-art models.

# About ailia SDK

[ailia SDK](https://ailia.jp/en/) is a cross-platform high speed inference SDK. The ailia SDK provides a consistent C++ API on Windows, Mac, Linux, iOS, Android and Jetson. It supports Unity, Python and JNI for efficient AI implementation. The ailia SDK makes great use of the GPU via Vulkan and Metal to serve accelerated computing.

# Supported models

## Action recognition

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [mars](/action_recognition/mars/) | [MARS: Motion-Augmented RGB Stream for Action Recognition](https://github.com/craston/MARS) | Pytorch | 1.2.4 beta and later | [<img src="action_recognition/mars/inputs/input0.jpg" width=64px>](action_recognition/mars/) |

## Crowd counting

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[crowdcount-cascaded-mtl](/crowd_counting/crowdcount-cascaded-mtl) | [CNN-based Cascaded Multi-task Learning of High-level Prior and Density Estimation for Crowd Counting (Single Image Crowd Counting)](https://github.com/svishwa/crowdcount-cascaded-mtl) | Pytorch | 1.2.1 and later | [<img src="crowd_counting/crowdcount-cascaded-mtl/result.png" height=64px>](crowd_counting/crowdcount-cascaded-mtl/) |

## Deep fashion

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [clothing-detection](/deep_fashion/clothing-detection/) | [Clothing-Detection](https://github.com/simaiden/Clothing-Detection) | Pytorch | 1.2.1 and later | [<img src="deep_fashion/clothing-detection/output_modanet.png" width=64px>](deep_fashion/clothing-detection/) |

## Depth estimation

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[monodepth2](depth_estimation/monodepth2)| [Monocular depth estimation from a single image](https://github.com/nianticlabs/monodepth2) | Pytorch | 1.2.2 and later | [<img src="depth_estimation/monodepth2/output.png" width=128px>](depth_estimation/monodepth2/) |
|[midas](depth_estimation/midas)| [Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer](https://github.com/intel-isl/MiDaS) | Pytorch | 1.2.4 beta and later | [<img src="depth_estimation/midas/input_depth.png" width=128px>](depth_estimation/midas/) |

## Face detection

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [yolov1-face](/face_detection/yolov1-face/) | [YOLO-Face-detection](https://github.com/dannyblueliu/YOLO-Face-detection/) | Darknet | 1.1.0 and later | [<img src="face_detection/yolov1-face/output.png" width=64px>](face_detection/yolov1-face/) |
| [yolov3-face](/face_detection/yolov3-face/) | [Face detection using keras-yolov3](https://github.com/axinc-ai/yolov3-face) | Keras | 1.2.1 and later | [<img src="face_detection/yolov3-face/output.png" width=64px>](face_detection/yolov3-face/) |
|[blazeface](/face_detection/blazeface/)| [BlazeFace-PyTorch](https://github.com/hollance/BlazeFace-PyTorch) | Pytorch | 1.2.1 and later | [<img src="face_detection/blazeface/result.png" width=64px>](face_detection/blazeface/) |
| [face-mask-detection](/face_detection/face-mask-detection/) | [Face detection using keras-yolov3](https://github.com/axinc-ai/yolov3-face) | Keras | 1.2.1 and later | [<img src="face_detection/face-mask-detection/output.png" width=64px>](face_detection/face-mask-detection/) |

## Face identification

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[vggface2](/face_identification/vggface2) | [VGGFace2 Dataset for Face Recognition](https://github.com/ox-vgg/vgg_face2) | Caffe | 1.1.0 and later | [<img src="face_identification/vggface2/couple_a.jpg" width=64px>](face_identification/vggface2/) |
|[arcface](/face_identification/arcface) | [pytorch implement of arcface](https://github.com/ronghuaiyang/arcface-pytorch) | Pytorch | 1.2.1 and later | [<img src="face_identification/arcface/correct_pair_1.jpg" width=64px>](face_identification/arcface/) |

## Face recognition

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[face_classification](/face_recognition/face_classification) | [Real-time face detection and emotion/gender classification](https://github.com/oarriaga/face_classification) | Keras | 1.1.0 and later | [<img src="face_recognition/face_classification/lenna.png">](face_recognition/face_classification/) |
|[facial_feature](/face_recognition/facial_feature/)|[kaggle-facial-keypoints](https://github.com/axinc-ai/kaggle-facial-keypoints)|Pytorch| 1.2.0 and later | [<img src="face_recognition/facial_feature/output.png" width=64px>](face_recognition/facial_feature/) |
|[face_alignment](/face_recognition/face_alignment/)| [2D and 3D Face alignment library build using pytorch](https://github.com/1adrianb/face-alignment) | Pytorch | 1.2.1 and later | [<img src="face_recognition/face_alignment/output.png" width=64px>](face_recognition/face_alignment/) |
|[prnet](/face_recognition/prnet)| [Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network](https://github.com/YadiraF/PRNet) | TensorFlow | 1.2.2 and later | [<img src="face_recognition/prnet/results/dense_alignment.png" width=64px>](face_recognition/prnet/) |
| [gazeml](/face_recognition/gazeml/) | [A deep learning framework based on Tensorflow for the training of high performance gaze estimation](https://github.com/swook/GazeML) | TensorFlow | 1.2.0 and later | [<img src="face_recognition/gazeml/output.png" width=64px>](face_recognition/gazeml/) |

## Generative adversarial networks

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[pytorch-gan](/generative_adversarial_networks/pytorch-gan) | [Code repo for the Pytorch GAN Zoo project (used to train this model)](https://github.com/facebookresearch/pytorch_GAN_zoo)| Pytorch | 1.2.4 beta and later | [<img src="generative_adversarial_networks/pytorch-gan/output_anime.png" width=64px>](generative_adversarial_networks/pytorch-gan/) |
|[council-GAN](/generative_adversarial_networks/council-GAN)| [Council-GAN](https://github.com/Onr/Council-GAN)| Pytorch | 1.2.4 beta and later | [<img src="generative_adversarial_networks/council-GAN/output_glasses.png" width=64px>](generative_adversarial_networks/council-GAN/) |

## Hand detection

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [yolov3-hand](/hand_detection/yolov3-hand/) | [Hand detection branch of Face detection using keras-yolov3](https://github.com/axinc-ai/yolov3-face/tree/hand_detection) | Keras | 1.2.1 and later | [<img src="hand_detection/yolov3-hand/output.png" width=64px>](hand_detection/yolov3-hand/) |

## Image captioning

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [illustration2vec](/image_captioning/illustration2vec/)|[Illustration2Vec](https://github.com/rezoo/illustration2vec) | Caffe | 1.2.2 and later | [<img src="image_captioning/illustration2vec/input.jpg" width=64@x>](image_captioning/illustration2vec/) |

## Image classification

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [vgg16](/image_classification/vgg16/) |[Very Deep Convolutional Networks for Large-Scale Image Recognition]( https://arxiv.org/abs/1409.1556 )|Keras| 1.1.0 and later| [<img src="image_classification/vgg16/clock.jpg" width=64px>](image_classification/vgg16/) |
| [googlenet](/image_classification/googlenet/) |[Going Deeper with Convolutions]( https://arxiv.org/abs/1409.4842 )|Pytorch| 1.2.0 and later| [<img src="image_classification/googlenet/pizza.jpg" width=64px>](image_classification/googlenet/) |
| [resnet50](/image_classification/resnet50/) | [Deep Residual Learning for Image Recognition]( https://github.com/KaimingHe/deep-residual-networks) | Chainer | 1.2.0 and later | [<img src="image_classification/resnet50/pizza.jpg" width=64px>](image_classification/resnet50/) |
| [inceptionv3](/image_classification/inceptionv3/)|[Rethinking the Inception Architecture for Computer Vision](http://arxiv.org/abs/1512.00567)|Pytorch| 1.2.0 and later | [<img src="image_classification/inceptionv3/clock.jpg" width=64px>](image_classification/inceptionv3/) |
| [mobilenetv2](/image_classification/mobilenetv2/)|[PyTorch Implemention of MobileNet V2](https://github.com/d-li14/mobilenetv2.pytorch)|Pytorch| 1.2.0 and later | [<img src="image_classification/mobilenetv2/clock.jpg" width=64px>](image_classification/mobilenetv2/) |
| [mobilenetv3](/image_classification/mobilenetv3/)|[PyTorch Implemention of MobileNet V3](https://github.com/d-li14/mobilenetv3.pytorch)|Pytorch| 1.2.1 and later | [<img src="image_classification/mobilenetv3/clock.jpg" width=64px>](image_classification/mobilenetv3/) |
| [partialconv](/image_classification/partialconv/)|[Partial Convolution Layer for Padding and Image Inpainting](https://github.com/NVIDIA/partialconv)|Pytorch| 1.2.0 and later | [<img src="image_classification/partialconv/test_5735.JPEG" width=64px>](image_classification/partialconv/) |
| [efficientnet](/image_classification/efficientnet/)|[A PyTorch implementation of EfficientNet]( https://github.com/lukemelas/EfficientNet-PyTorch)|Pytorch| 1.2.3 and later | [<img src="image_classification/efficientnet/clock.jpg" width=64px>](image_classification/efficientnet/) |

## Image manipulation

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [noise2noise](/image_maniplulation/noise2noise/) | [Learning Image Restoration without Clean Data](https://github.com/joeylitalien/noise2noise-pytorch) | Pytorch | 1.2.0 and later | [<img src="image_manipulation/noise2noise/output.png" width=64px>](image_manipulation/noise2noise/) |
| [dewarpnet](/image_maniplulation/dewarpnet) | [DewarpNet: Single-Image Document Unwarping With Stacked 3D and 2D Regression Networks](https://github.com/cvlab-stonybrook/DewarpNet) | Pytorch | 1.2.1 and later | [<img src="image_manipulation/dewarpnet/output.png" width=64px>](image_manipulation/dewarpnet/) |
| [illnet](/image_maniplulation/illnet/) | [Document Rectification and Illumination Correction using a Patch-based CNN](https://github.com/xiaoyu258/DocProj) | Pytorch | 1.2.2 and later | [<img src="image_manipulation/illnet/output.png" width=64px>](image_manipulation/illnet/) |

## Image segmentation

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [deeplabv3](/image_segmentation/deeplabv3/) | [Xception65 for backbone network of DeepLab v3+](https://github.com/tensorflow/models/tree/master/research/deeplab) | Chainer | 1.2.0 and later | [<img src="image_segmentation/deeplabv3/output.png" width=64px>](image_segmentation/deeplabv3/) |
| [hrnet_segmentation](/image_segmentation/hrnet_segmentation/) | [High-resolution networks (HRNets) for Semantic Segmentation](https://github.com/HRNet/HRNet-Semantic-Segmentation) | Pytorch | 1.2.1 and later | [<img src="image_segmentation/hrnet_segmentation/result.png" width=64px>](image_segmentation/hrnet_segmentation/) |
| [hair_segmentation](/image_segmentation/hair_segmentation/) | [hair segmentation in mobile device](https://github.com/thangtran480/hair-segmentation) | Keras | 1.2.1 and later | [<img src="image_segmentation/hair_segmentation/output.png" width=64px>](image_segmentation/hair_segmentation/) |
| [pspnet-hair-segmentation](/image_segmentation/pspnet-hair-segmentation/) | [pytorch-hair-segmentation](https://github.com/YBIGTA/pytorch-hair-segmentation) | Pytorch | 1.2.2 and later | [<img src="image_segmentation/pspnet-hair-segmentation/output.png" width=64px>](image_segmentation/pspnet-hair-segmentation/) |
| [U-2-Net](/image_segmentation/u2net/) | [U^2-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://github.com/NathanUA/U-2-Net) | Pytorch | 1.2.2 and later | [<img src="image_segmentation/u2net/output.png" width=64px>](image_segmentation/u2net/) |
| [deep-image-matting](/image_segmentation/deep-image-matting/) | [Deep Image Matting](https://github.com/foamliu/Deep-Image-Matting)| Keras | 1.2.3 and later | [<img src="image_segmentation/deep-image-matting/output.png" width=64px>](image_segmentation/deep-image-matting/) |

## Natural language processing

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[bert](/neural_language_processing/bert) | [pytorch-pretrained-bert](https://pypi.org/project/pytorch-pretrained-bert/) | Pytorch | 1.2.2 and later | |

## Object detection

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [yolov1-tiny](/object_detection/yolov1-tiny/) | [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolov1/) | Darknet | 1.1.0 and later | [<img src="object_detection/yolov1-tiny/output.png" width=64px>](object_detection/yolov1-tiny/) |
| [yolov2](/object_detection/yolov2/) | [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/) | Pytorch | 1.2.0 and later | [<img src="object_detection/yolov2/output.png" width=64px>](object_detection/yolov2/) |
| [yolov3](/object_detection/yolov3/) | [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/) | ONNX Runtime | 1.2.1 and later | [<img src="object_detection/yolov3/output.png" width=64px>](object_detection/yolov3/) |
| [yolov3-tiny](/object_detection/yolov3-tiny/) | [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/) | ONNX Runtime | 1.2.1 and later | [<img src="object_detection/yolov3-tiny/output.png" width=64px>](object_detection/yolov3-tiny/) |
| [yolov4](/object_detection/yolov4/) | [Pytorch-YOLOv4](https://github.com/Tianxiaomo/pytorch-YOLOv4) | Pytorch | 1.2.4 beta and later | [<img src="object_detection/yolov4/output.png" width=64px>](object_detection/yolov4/) |
| [mobilenet_ssd](/object_detection/mobilenet_ssd/) | [MobileNetV1, MobileNetV2, VGG based SSD/SSD-lite implementation in Pytorch](https://github.com/qfgaohao/pytorch-ssd) | Pytorch | 1.2.1 and later | [<img src="object_detection/mobilenet_ssd/annotated.png" width=64px>](object_detection/mobilenet_ssd/) |
| [maskrcnn](/object_detection/maskrcnn/) | [Mask R-CNN: real-time neural network for object instance segmentation](https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/mask-rcnn) | Pytorch | 1.2.3 and later | [<img src="object_detection/maskrcnn/output.png" width=64px>](object_detection/maskrcnn/) |
| [m2det](/object_detection/m2det/) | [M2Det: A Single-Shot Object Detector based on Multi-Level Feature Pyramid Network](https://github.com/qijiezhao/M2Det) | Pytorch | 1.2.3 and later | [<img src="object_detection/m2det/output.png" width=64px>](object_detection/m2det/) |
| [centernet](/object_detection/centernet/) | [CenterNet : Objects as Points](https://github.com/xingyizhou/CenterNet) | Pytorch | 1.2.1 and later | [<img src="object_detection/centernet/output.png" width=64px>](object_detection/centernet/) |

## Object tracking

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [deepsort](/object_tracking/deepsort/) | [Deep Sort with PyTorch](https://github.com/ZQPei/deep_sort_pytorch) | Pytorch | 1.2.3 and later | [<img src="object_tracking/deepsort/demo.gif" width=64px>](object_tracking/deepsort/) |

## Pose estimation

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[openpose](/pose_estimation/openpose/) | [Code repo for realtime multi-person pose estimation in CVPR'17 (Oral)](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation) | Caffe | 1.2.1 and later | [<img src="pose_estimation/openpose/output.png" width=64px>](pose_estimation/openpose/) |
|[lightweight-human-pose-estimation](/pose_estimation/lightweight-human-pose-estimation/) | [Fast and accurate human pose estimation in PyTorch. Contains implementation of "Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose" paper.](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch) | Pytorch | 1.2.1 and later | [<img src="pose_estimation/lightweight-human-pose-estimation/output.png" width=64px>](pose_estimation/lightweight-human-pose-estimation/) |
|[lightweight-human-pose-estimation-3d](/pose_estimation/lightweight-human-pose-estimation-3d/) | [Real-time 3D multi-person pose estimation demo in PyTorch. OpenVINO backend can be used for fast inference on CPU.](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation-3d-demo.pytorch) | Pytorch | 1.2.1 and later | [<img src="pose_estimation/lightweight-human-pose-estimation-3d/ICV_3D_Human_Pose_Estimation_0.png" width=64px>](pose_estimation/lightweight-human-pose-estimation-3d/) |
|[3d-pose-baseline](/pose_estimation/3d-pose-baseline/) | [A simple baseline for 3d human pose estimation in tensorflow. Presented at ICCV 17.](https://github.com/una-dinosauria/3d-pose-baseline) | Tensorflow | 1.2.3 and later | [<img src="pose_estimation/3d-pose-baseline/output.png" width=64px>](pose_estimation/3d-pose-baseline/) |
|[pose_resnet](/pose_estimation/pose_resnet/) | [Simple Baselines for Human Pose Estimation and Tracking](https://github.com/microsoft/human-pose-estimation.pytorch) | Pytorch | 1.2.1 and later | [<img src="pose_estimation/pose_resnet/output.png" width=64px>](pose_estimation/pose_resnet/) |

## Rotation prediction

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[rotnet](/rotation_prediction/rotnet) | [CNNs for predicting the rotation angle of an image to correct its orientation](https://github.com/d4nst/RotNet) | Keras | 1.2.1 and later | [<img src="rotation_prediction/rotnet/output.png" width=256px>](rotation_prediction/rotnet/) |

## Style transfer

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [adain](/style_transfer/adain/) | [Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization](https://github.com/naoto0804/pytorch-AdaIN)| Pytorch | 1.2.1 and later | [<img src="style_transfer/adain/output.png" width=64px>](style_transfer/adain/) |

## Super resolution

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
| [srresnet](/super_resolution/srresnet/) | [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://github.com/twtygqyy/pytorch-SRResNet) | Pytorch | 1.2.0 and later | [<img src="super_resolution/srresnet/output.png" width=64px>](super_resolution/srresnet/) |

## Text recognition

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[etl](/text_recognition/etl) | Japanese Character Recognization | Keras | 1.1.0 and later | [<img src="text_recognition/etl/font.png" width=64px>](text_recognition/etl/) |

## Commercial model

| Name | Detail | Exported From | Supported Ailia Version | Demo |
|:-----------|------------:|:------------:|:------------:|:------------:|
|[acculus-pose](/commercial_model/acculus-pose) | [Acculus, Inc.](https://acculus.jp/) | Caffe | 1.2.3 and later |

# Setup

## Install ailia SDK

- [Download a free evaluation version of ailia SDK](https://ailia.jp/en/trial)
- Unzip ailia SDK
- Find the location of Python site-packages directory
```
python -c "import site; print (site.getsitepackages())"
```

- Copy the ​ailia ​folder located in the ​python f​older to site-packages
- Copy library files (dll or dylib or so) from the folder library to site-packages/ailia
- In the evaluation version, place the license file in the same folder as libailia.dll on Windows and in ~/Library/SHALO/ on Mac.

## Install required libraries for Python

### For Windows, Mac, Linux

```
pip install -r requirements.txt
```

### For Jetson

```
sudo apt install python3-pip
sudo apt install python3-matplotlib
sudo apt install python3-scipy
pip3 install cython
pip3 install numpy
```

[OpenCV for python3 is pre-installed on Jetson.](https://forums.developer.nvidia.com/t/install-opencv-for-python3-in-jetson-nano/74042/3) You only need to run this command if you get a cv2 import error.

```
sudo apt install python3-opencv
```