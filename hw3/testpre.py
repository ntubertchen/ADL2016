import sys
filename = sys.argv[1]
test_in = open("./data/ATIS/test/test.seq.in","w")
test_out = open("./data/ATIS/test/test.seq.out","w")
test_label = open("./data/ATIS/test/test.label","w")
with open(filename,'r') as testing_data:
		for line in testing_data:
			line = line.strip().split()
			S_num = line.index("EOS")
			S_in = line[1:line.index("EOS")]
			for i in range(len(S_in)):
				test_in.write(S_in[i])
				test_in.write(" ")
			test_in.write("\n")
			for i in range(S_num-1):
				test_out.write("O ")
			test_out.write("\n")
			test_label.write("flight\n")
test_in.close()
test_out.close()
test_label.close()