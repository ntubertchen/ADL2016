#!/bin/bash
python out.py --decode --train_dir ./Translatemodel --data_dir ./Translatedata --size=256 --num_layers=2 --test_dir ${1} --answer_dir ${2}