#!/bin/bash
python word2vec_skipgram.py --train_data $1 --eval_data $1 --save_path ./ > word2vec_skip.txt
python filterVocab.py fullVocab.txt < word2vec_skip.txt > $2filter_word2vec.txt
python word2vec_GloVe.py $1 > word2vec_glove.txt
python filterVocab.py fullVocab.txt < word2vec_glove.txt > $2filter_glove.txt
rm -rf word2vec_skip.txt
rm -rf word2vec_glove.txt