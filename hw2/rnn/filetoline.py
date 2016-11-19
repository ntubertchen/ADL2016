left = 0
right = 0
sentence = ""
with open('./rnn/pos.txt','r') as f:
	with open('./rnn/trees/pos_line.txt','w') as w:
		for line in f:
			left += line.count("(")
			right += line.count(")")
			if line.count('None') is 0 and line.count("(") is not 0 or line.count(")") is not 0:
				sentence += line
			if left is right and left > 0:
				sentence = sentence.replace('\n','')
				w.write(sentence)
				w.write("\n")
				sentence = ""
				left = 0
				right = 0

left = 0
right = 0
sentence = ""
with open('./rnn/neg.txt','r') as f:
	with open('./rnn/trees/neg_line.txt','w') as w:
		for line in f:
			left += line.count("(")
			right += line.count(")")
			if line.count('None') is 0 and line.count("(") is not 0 or line.count(")") is not 0:
				sentence += line
			if left is right and left > 0:
				sentence = sentence.replace('\n','')
				w.write(sentence)
				w.write("\n")
				sentence = ""
				left = 0
				right = 0

left = 0
right = 0
sentence = ""
with open('./rnn/test.txt','r') as f:
	with open('./rnn/trees/test_line.txt','w') as w:
		for line in f:
			left += line.count("(")
			right += line.count(")")
			if line.count('None') is 0 and line.count("(") is not 0 or line.count(")") is not 0:
				sentence += line
			if left is right and left > 0:
				sentence = sentence.replace('\n','')
				w.write(sentence)
				w.write("\n")
				sentence = ""
				left = 0
				right = 0
