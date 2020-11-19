from transformers import AutoTokenizer

import numpy
import time
import sys
import argparse

import ailia

sys.path.append('../../util')
from model_utils import check_and_download_models  # noqa: E402

# ======================
# Arguemnt Parser Config
# ======================

SENTENCE = "Who are you voting for in 2020?"
CANDIDATE_LABELS = "economics, politics, public health"

parser = argparse.ArgumentParser(
    description='bert zero-shot-classification.'
)

parser.add_argument(
    '--sentence', '-s', metavar='TEXT',
    default=SENTENCE, 
    help='input text'
)
parser.add_argument(
    '--candidate_labels', '-c', metavar='TEXT',
    default=CANDIDATE_LABELS, 
    help='input text'
)
parser.add_argument(
    '-b', '--benchmark',
    action='store_true',
    help='Running the inference on the same input 5 times ' +
         'to measure execution performance. (Cannot be used in video mode)'
)
args = parser.parse_args()


# ======================
# PARAMETERS
# ======================

WEIGHT_PATH = "roberta-large-mnli.onnx"
MODEL_PATH = "roberta-large-mnli.onnx.prototxt"
REMOTE_PATH = "https://storage.googleapis.com/ailia-models/bert_zero_shot_classification/"


# ======================
# Main function
# ======================
def main():
    # model files check and download
    check_and_download_models(WEIGHT_PATH, MODEL_PATH, REMOTE_PATH)

    candidate_labels = CANDIDATE_LABELS.split(", ")

    ailia_model = ailia.Net(MODEL_PATH,WEIGHT_PATH)
    tokenizer = AutoTokenizer.from_pretrained('roberta-large-mnli"')
    model_inputs = tokenizer.encode_plus(args.input, return_tensors="pt")
    inputs_onnx = {k: v.cpu().detach().numpy() for k, v in model_inputs.items()}

    print("Input : ", args.input)

    # inference
    if args.benchmark:
        print('BENCHMARK mode')
        for i in range(5):
            start = int(round(time.time() * 1000))
            score = ailia_model.predict(inputs_onnx)
            end = int(round(time.time() * 1000))
            print("\tailia processing time {} ms".format(end - start))
    else:
        score = ailia_model.predict(inputs_onnx)

    score = numpy.exp(score) / numpy.exp(score).sum(-1, keepdims=True)

    label_id=numpy.argmax(numpy.array(score))
    print("Label : ",candidate_labels[label_id])
    print("Score : ",score[0][0][label_id])

    print('Script finished successfully.')

if __name__ == "__main__":
    main()
