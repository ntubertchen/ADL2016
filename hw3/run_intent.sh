#!/bin/bash
python testpre.py ${1}
answer_file=${2}
data_dir=data/ATIS
model_dir=model_intent
max_sequence_length=50  # max length for train/valid/test sequence
task=intent  # available options: intent; tagging; joint
bidirectional_rnn=True  # available options: True; False

python run_multi-task_rnn.py --data_dir $data_dir \
      --train_dir   $model_dir\
      --max_sequence_length $max_sequence_length \
      --task $task \
      --bidirectional_rnn $bidirectional_rnn \
      --answer_file $answer_file
