from nltk.util import ngrams
import sys, getopt

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def dna_filter(sequence):
	dna = sequence.split(dna_mark, 1)[1].replace(" ", "").replace("\n", "")
	dna_filtered = ''.join(i for i in dna if not i.isdigit())
	return dna_filtered

dna_mark = "ORIGIN"

def main(argv):
	inputfile = ''
	char = ''
	dna_file = ''
	motifs_file = ''
	features_file = ''
	n = 0
	m = 0
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","char=","dna=","motifs=","features=","min=","max="])
	except getopt.GetoptError as e:
		print('parsing.py -i <inputfile> -c <char> -d <dna> -mo <motifs> -f <features> -min <min> -max <max>')
		print(e)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('parsing.py -i <inputfile> -c <char> -d <dna> -m <motifs> -f <features> -min <min> -max <max>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-c", "--char"):
			char = arg
		elif opt in ("-d", "--dna"):
			dna_file = arg
		elif opt in ("-m", "--motifs"):
			motifs_file = arg
		elif opt in ("-f", "--features"):
			features_file = arg
		elif opt in ("--min"):
			# N-Grams min range
			n = int(arg)
		elif opt in ("--max"):
			# N-Grams max range
			m = int(arg)

	print ('Input file is ', inputfile)
	print ('DNA file is ', dna_file)
	print ('char is ', char)
	print ('Motifs file is ', motifs_file)
	print ('Features file is ', features_file)
	print ('N-gram min length ', n)
	print ('N-gram max length ', m) 

	all_grams = []
	number = 0

	# open file
	fyle = open(inputfile)
	dna = open(dna_file, 'w')
	motifs = open(motifs_file, 'w')
	features = open(features_file, 'w')
	# delete file content before writing
	deleteContent(dna)
	deleteContent(motifs)
	# read file
	data = fyle.read()
	# split data into sequences
	sequences = data.split("//")

	for sequence in sequences:
		if len(sequence) > 3000 and char in sequence:
			number += 1
			# write DNA to result.gb
			sequence_id = sequence.split()[1]
			dna_string = dna_filter(sequence)
			dna.write(">" + sequence_id + '\n') # sequence id
			dna.write(dna_string + '\n' + '//' + '\n')
			# exact into motifs and write to motifs.gb
			motifs.write(sequence_id + '\n')
			for N in range(n, m+1):
				grams = ngrams(list(dna_string), N)
				temp = []
				for gram in grams:
					# append tuple to temp
					temp.append(gram)
					motifs.write(''.join(str(s) for s in gram) + '\n')
				# extend temp list to all_grams
				all_grams.extend(temp)
			motifs.write('//\n')

	# create distinct motifs (features)
	distinct_grams = set(all_grams)
	for gram in distinct_grams:
		features.write(''.join(str(s) for s in gram) + '\n')
	print(str(number) + ' sequences')

	fyle.close()
	dna.close()
	motifs.close()
	features.close()

if __name__ == "__main__":
   main(sys.argv[1:])
