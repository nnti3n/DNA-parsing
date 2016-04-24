import sys, getopt
from itertools import islice
import time
from collections import Counter

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def read_in_chunks(file_path, n):
	with open(file_path) as fh:
		while True:
			lines = list(islice(fh, n))
			if lines: yield lines
			else:     
				break

def main(argv):
	inputfile = ''
	outputfile = ''
	n = 0
	m = 0
	try:
		opts, args = getopt.getopt(argv,"hi:o:f:m:",["input=","output=","features=","max="])
	except getopt.GetoptError as e:
		print('parsing.py -i <inputfile> -m <max> -o <output>')
		print(e)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('parsing_lage.py -i <inputfile> -m <max> -o <output>')
			sys.exit()
		elif opt in ("-i", "--input"):
			inputfile = arg
		elif opt in ("-m", "--max"):
			m = arg
		elif opt in ("-o", "--output"):
			outputfile = arg
		elif opt in ("-f", "--features"):
			featuresfile = arg

	print ('Input file is ', inputfile)
	print ('Output file ', outputfile)
	# print ('Features file ', featuresfile)
	print ('max features ', m)

	# time
	start_time = time.time()

	# number of seq counter
	number = 0
	occur = 0
	lines = []
	total = []

	# open file
	fyle = open(inputfile)
	output = open(outputfile, 'w')
	# features = open(featuresfile, 'w')
	# delete file content before writing
	deleteContent(output)
	# deleteContent(features)

	# with open(inputfile, 'r') as inF:
	# 	for motif in inF:
	# 		occur = 0
	# 		number += 1
	# 		if motif in total:
	# 			continue
	# 		for lines in read_in_chunks(inputfile, 10000):
	# 			for line in lines:
	# 				if line == motif:
	# 					occur += 1
	# 		print("--- %s seconds ---" % (time.time() - start_time))

	# 		print(number)
	# 		output.write(motif.replace(" ", "").replace("\n", "") + " " + str(occur-1) + "\n")
	# 		total.append(motif)

	data = fyle.read();
	motifs = Counter(data.split());
	print(len(motifs))

	# create distinct motifs (features)
	# distinct_grams = set(motifs)
	# print(len(distinct_grams))

	count_motif = 0
	same_motif = ""
	# 70% occurence
	# for gram in distinct_grams:
	# 	number += 1
	# 	count_motif = 0
	# 	# str_gram = ''.join(gram)
	# 	if (len(same_motif) > 0):
	# 		motifs = list(filter((same_motif).__ne__, motifs))
	# 	for motif in motifs:
	# 		if gram == motif:
	# 			count_motif += 1
	# 	if count_motif > 1:
	# 		same_motif = gram
	# 	else:
	# 		same_motif = ""
	# 	output.write(str(count_motif) + " " + gram + "\n")
	# 	print("--- %s seconds ---" % (time.time() - start_time))
	# 	print(number)

	# for gram in motifs_most:
	# 	features.write(gram + '\n')

	for key, value in motifs.most_common(int(m)):
		number += 1
		# output.write(key + " " + str(value) + "\n")
		output.write(key + "\n")
		# features.write(key + "\n")
		print(number)

	print("--- %s seconds ---" % (time.time() - start_time))

	# print(number)

	fyle.close()
	output.close()

if __name__ == "__main__":
	main(sys.argv[1:])