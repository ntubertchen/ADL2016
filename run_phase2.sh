#!/bin/bash
python word2vec_phase2.py --train_data $1 --eval_data $1 --save_path ./ > phase2_vec.txt
python filterVocab.py fullVocab_phase2.txt < phase2_vec.txt > $2filter_vec.txt
rm -rf phase2_vec.txt