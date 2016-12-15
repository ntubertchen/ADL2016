#!/bin/bash
python out.py --decode --train_dir ./NLGmodel --data_dir ./NLGdata --size=256 --num_layers=2 --test_dir ${1} --answer_dir ${2}