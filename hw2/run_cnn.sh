#!/bin/bash
python ./cnn/train.py ${1}
python ./cnn/eval.py --eval_train --checkpoint_dir="./runs/output/checkpoints/" ${1}
python ./cnn/out.py ${2}
rm -rf ./prediction.csv
