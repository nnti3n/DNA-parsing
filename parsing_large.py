import sys, getopt
from itertools import islice
import time

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
		opts, args = getopt.getopt(argv,"hi:o:",["input=","output="])
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
		# elif opt in ("-m", "--max"):
		# 	m = arg
		elif opt in ("-o", "--output"):
			outputfile = arg

	print ('Input file is ', inputfile)
	print ('Output file ', outputfile)

	# time
	start_time = time.time()

	# number of seq counter
	number = 0
	occur = 0
	lines = []
	total = []

	# open file
	# fyle = open(inputfile)
	output = open(outputfile, 'w')
	# delete file content before writing
	deleteContent(output)

	with open(inputfile, 'r') as inF:
		for motif in inF:
			occur = 0
			number += 1
			if motif in total:
				continue
			for lines in read_in_chunks(inputfile, 10000):
				for line in lines:
					if line == motif:
						occur += 1
			print("--- %s seconds ---" % (time.time() - start_time))

			print(number)
			output.write(motif.replace(" ", "").replace("\n", "") + " " + str(occur-1) + "\n")
			total.append(motif)

	print(number)

	# fyle.close()
	output.close()

if __name__ == "__main__":
	main(sys.argv[1:])