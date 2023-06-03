﻿import os
import sys
import time

import numpy as np
import librosa
import soundfile as sf

import ailia

# import original modules
sys.path.append('../../util')
from arg_utils import get_base_parser, update_parser, get_savepath  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
# logger
from logging import getLogger  # noqa: E402

logger = getLogger(__name__)

# ======================
# Parameters
# ======================

WEIGHT_PATH = 'silero_vad.onnx'
MODEL_PATH = None#'silero_vad.onnx.onnx.prototxt'
REMOTE_PATH = 'https://storage.googleapis.com/ailia-models/silero-vad/'

WAVE_PATH = "en_example.wav"
SAVE_PATH = 'only_speech.wav'

# Audio
SAMPLING_RATE = 16000

# ======================
# Arguemnt Parser Config
# ======================

parser = get_base_parser(
    'VoiceFilter', WAVE_PATH, SAVE_PATH, input_ftype='audio'
)
parser.add_argument(
    '-r', '--reference_file',
    default="ref-voice.wav", type=str,
    help='path of reference wav file'
)
args = update_parser(parser)

# ======================
# Logic
# ======================





dependencies = ['torch', 'torchaudio']
import torch
import json
import os
from utils_vad import (get_speech_timestamps,
                       save_audio,
                       read_audio,
                       VADIterator,
                       collect_chunks,
                       OnnxWrapper)

def silero_vad(onnx=False, force_onnx_cpu=False):
    model = OnnxWrapper('silero_vad.onnx', force_onnx_cpu)
    utils = (get_speech_timestamps,
             save_audio,
             read_audio,
             VADIterator,
             collect_chunks)

    return model, utils

def audio_recognition():
  SAMPLING_RATE = 16000

  import torch
  torch.set_num_threads(1)

  #from IPython.display import Audio
  from pprint import pprint

  # %%
  USE_ONNX = True # change this to True if you want to test onnx model
    
  model, utils = silero_vad(onnx = True)

  (get_speech_timestamps,
  save_audio,
  read_audio,
  VADIterator,
  collect_chunks) = utils

  # **Speech timestapms from full audio**

  # %%
  wav = read_audio('en_example.wav', sampling_rate=SAMPLING_RATE)
  # get speech timestamps from full audio file
  speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=SAMPLING_RATE)
  pprint(speech_timestamps)

  # %%
  # merge all speech chunks to one audio
  save_audio('only_speech.wav',
            collect_chunks(speech_timestamps, wav), sampling_rate=SAMPLING_RATE) 
  #Audio('only_speech.wav')

  # %% [markdown]
  # ## Stream imitation example

  # %%
  ## using VADIterator class

  vad_iterator = VADIterator(model)
  wav = read_audio(f'en_example.wav', sampling_rate=SAMPLING_RATE)

  window_size_samples = 1536 # number of samples in a single audio chunk
  for i in range(0, len(wav), window_size_samples):
      chunk = wav[i: i+ window_size_samples]
      if len(chunk) < window_size_samples:
        break
      speech_dict = vad_iterator(chunk, return_seconds=True)
      if speech_dict:
          print(speech_dict, end=' ')
  vad_iterator.reset_states() # reset model states after each audio

  # %%
  ## just probabilities

  wav = read_audio('en_example.wav', sampling_rate=SAMPLING_RATE)
  speech_probs = []
  window_size_samples = 1536
  for i in range(0, len(wav), window_size_samples):
      chunk = wav[i: i+ window_size_samples]
      if len(chunk) < window_size_samples:
        break
      speech_prob = model(chunk, SAMPLING_RATE).item()
      speech_probs.append(speech_prob)
  vad_iterator.reset_states() # reset model states after each audio

  print(speech_probs[:10]) # first 10 chunks predicts


# ======================
# Main
# ======================







def main():
    # model files check and download
    check_and_download_models(WEIGHT_PATH, MODEL_PATH, REMOTE_PATH)

    #env_id = args.env_id

    #net = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=env_id)
    #embedder = ailia.Net(MODEL_EMB_PATH, WEIGHT_EMB_PATH, env_id=env_id)

    audio_recognition()


if __name__ == '__main__':
    main()