# ADL2016
Synopsis
	This homework includes two parts. First, we use free resources from wikipedia to train word2vec. 
	We use two different approachs to train our word2vec model, skipgram and GloVe.
	Second, we try to perdict relations between words. Using a pre-trained word2vec model, we can use a vector-like method to find our word.
	The goal is to solve the following problem. C1:C2=C3:?
	We need to find a C4 that matchs such relationship.
API Reference
	One can use: bash run_phase1.sh corpus/text8 output_phase1/ to run phase1 code.
	As for phase2, please use: bash run_phase2.sh corpus/ptt_corpus.txt output_phase2/
	Our output vector will end up in the directory you want.

Report
GloVe
Acc:0.4462
batch_size=256, learning_rate=0.1,num_epochs=100,embedding_size=128

Acc:0.4294
batch_size=500, learning_rate=0.1,num_epochs=50,embedding_size=128

Acc:0.3774
batch_size=500, learning_rate=0.1,num_epochs=100,embedding_size=128

Acc:0.3117
batch_size=256, learning_rate=0.1,num_epochs=130,embedding_size=300

Acc:0.3188
batch_size=128, learning_rate=0.05,num_epochs=110,embedding_size=280

Acc:0.3461
batch_size=256,learning_rate=0.05,num_epochs=120,embedding_size=300

Acc:0.2946
batch_size=256, learning_rate=0.05,num_epochs=100,embedding_size=350

Acc:0.3038
batch_size=512,learning_rate=0.05,num_epochs=100,embedding_size=300

Acc:0.4048
batch_size=256, learning_rate=0.1,num_epochs=150,embedding_size=300

As far as I can tell, we need to find the perfect embedding size for our corpus. We can easily reach high accuracy form high learning
rate, normal training epoch and small embedding size. However, once we want to process more complex meaning, we need more training epoch
and larger embedding size for complicated corpus. Consequently, it takes more time for one model to be completed.

Skipgram
Acc:0.6558
I tried other method to gain better accuracy. But since I began my phase2. I lost all my record.

Phase2
It takes a hundred hours(CPU time) to train one model with 62.67 model.
The corpus is too big and it takes too much time for me to test other combination.
Still, since the corpus is too big, it still takes many epoch to come with a reasonable accuracy.
