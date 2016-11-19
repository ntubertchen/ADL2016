import csv
import sys
answerpath = sys.argv[1] + "answer.txt"
f = open(answerpath,'w') 
with open('prediction.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	i = 0
	for row in spamreader:
		f.write(row[len(row) - 1][0])
		f.write("\n")
		i += 1
		if not(i < 1000):
			break