#!/bin/bash
python3 ./rnn/preprocess.py ${2} training_data.pos.tree > ./rnn/pos.txt
python3 ./rnn/preprocess.py ${2} training_data.neg.tree > ./rnn/neg.txt
python3 ./rnn/preprocess.py ${2} testing_data.txt.tree > ./rnn/test.txt
python ./rnn/filetoline.py
rm -rf ./rnn/pos.txt
rm -rf ./rnn/neg.txt
rm -rf ./rnn/test.txt
python ./rnn/rnn_static_graph.py ${3}

