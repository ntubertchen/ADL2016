import sys
import random
random.seed(10)
filename = sys.argv[1]
train_in = open("train.seq.in","w")
train_out = open("train.seq.out","w")
train_label = open("train.label","w")
valid_in = open("valid.seq.in","w")
valid_out = open("valid.seq.out","w")
valid_label = open("valid.label","w")
with open(filename,'r') as training_data:
		for line in training_data:
			line = line.strip().split()
			S_in = line[1:line.index("EOS")]
			S_out = line[line.index("EOS") + 2:len(line)-1]
			S_label = line[len(line)-1]
			if random.random() > 0.01:
				for i in range(len(S_in)):
					train_in.write(S_in[i])
					train_in.write(" ")
				train_in.write("\n")
				for i in range(len(S_out)):
					train_out.write(S_out[i])
					train_out.write(" ")
				train_out.write("\n")
				for i in range(len(S_label)):
					train_label.write(S_label[i])
				train_label.write("\n")
			else:
				for i in range(len(S_in)):
					valid_in.write(S_in[i])
					valid_in.write(" ")
				valid_in.write("\n")
				for i in range(len(S_out)):
					valid_out.write(S_out[i])
					valid_out.write(" ")
				valid_out.write("\n")
				for i in range(len(S_label)):
					valid_label.write(S_label[i])
				valid_label.write("\n")
train_in.close()
train_out.close()
train_label.close()
valid_in.close()
valid_out.close()
valid_label.close()