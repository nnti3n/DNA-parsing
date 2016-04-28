from nltk.util import ngrams
import sys, getopt

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def dna_filter(sequence):
	dna = sequence.split(dna_mark, 1)[1].replace(" ", "").replace("\n", "")
	dna_filtered = ''.join(i for i in dna if not i.isdigit())
	return dna_filtered

def f(x):
    return {
        'subtype: A1': 'A1',
        'subtype: A2': 'A2',
        'subtype: A5': 'A5',
        'subtype: B1': 'B1',
        'subtype: B2': 'B2',
        'subtype: C1': 'C1',
        'subtype: C2': 'C2',
        'subtype: C4': 'C4',
        'subtype: D1': 'D1',
        'subtype: D2': 'D2',
        'subtype: D3': 'D3',
        'subtype: D4': 'D4',
        'subtype: D5': 'D5',
        'subtype: F1': 'F1',
        'subtype: F4': 'F4',
        'genotype: A1': 'A1',
        'genotype: A2': 'A2',
        'genotype: A5': 'A5',
        'genotype: B1': 'B1',
        'genotype: B2': 'B2',
        'genotype: C1': 'C1',
        'genotype: C2': 'C2',
        'genotype: C4': 'C4',
        'genotype: D1': 'D1',
        'genotype: D2': 'D2',
        'genotype: D3': 'D3',
        'genotype: D4': 'D4',
        'genotype: D5': 'D5',
        'genotype: F1': 'F1',
        'genotype: F4': 'F4',
        'genotype A1;': 'A1',
        'genotype A2;': 'A2',
        'genotype A5;': 'A5',
        'genotype B1;': 'B1',
        'genotype B2;': 'B2',
        'genotype C1;': 'C1',
        'genotype C2;': 'C2',
        'genotype C4;': 'C4',
        'genotype D1;': 'D1',
        'genotype D2;': 'D2',
        'genotype D3;': 'D3',
        'genotype D4;': 'D4',
        'genotype D5;': 'D5',
        'genotype F1;': 'F1',
        'genotype F4;': 'F4',
    }.get(x)

def subtype(sequence, chars):
	for char in chars:
		if char in sequence:
			return f(char)
	return False


dna_mark = "ORIGIN"

def main(argv):
	inputfile = ''
	# char = ''
	dna_file = ''
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
			print('parsing.py -i <inputfile> -c <char> -d <dna> -f <features> -min <min> -max <max>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		# elif opt in ("-c", "--char"):
		# 	char = arg
		elif opt in ("-d", "--dna"):
			dna_file = arg
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
	# print ('char is ', char)
	print ('Features file is ', features_file)
	print ('N-gram min length ', n)
	print ('N-gram max length ', m) 

	all_grams = []
	temp_dna = []
	chars = ["subtype: A1", "subtype: A2", "subtype: A5", "subtype: B1", "subtype: B2", "subtype: C1", "subtype: C2",
	"subtype: C4", "subtype: F1", "subtype: D1", "subtype: D2", "subtype: D3",
	"subtype: D4", "subtype: D5", "subtype: F1", "subtype: F4", "genotype: A1", "genotype: A2",
	"genotype: A5", "genotype: B1", "genotype: B2", "genotype: C1", "genotype: C2",
	"genotype: C4", "genotype: D1", "genotype: D2",
	"genotype: D3", "genotype: D4", "genotype: D5", "genotype: F1", 
	"genotype: F4", "genotype A1;", "genotype A2;", "genotype A5;", "genotype B1;", 
	"genotype B2;", "genotype C1;", "genotype C2;",
	"genotype C4;", "genotype D1;", "genotype D2;", "genotype D3;",
	"genotype D4;", "genotype D5;", "genotype F1;", "genotype F4;"]
	# number of seq counter
	number = 0

	# open file
	fyle = open(inputfile)
	dna = open(dna_file, 'w')
	features = open(features_file, 'w')
	# delete file content before writing
	deleteContent(dna)
	# read file
	data = fyle.read()
	# split data into sequences
	sequences = data.split("//")

	for sequence in sequences:
		subtype_string = subtype(sequence, chars)
		if len(sequence) > 3000 and subtype_string:
			# write DNA to result.gb
			if sequence.split()[0] == 'LOCUS':
				sequence_id = sequence.split()[1]
				dna_string = dna_filter(sequence)
				if 'n' in dna_string:
					continue
				number += 1
			else:
				continue
			temp_dna.append(dna_string)
			dna.write(">" + sequence_id + '\n') # sequence id
			dna.write(subtype_string + '\n')
			# dna.write(dna_string + '\n' + '//' + '\n')
			dna.write('//\n')
			features.write(">" + sequence_id + '\n')
			# exact into motifs and write to motifs.gb
			for N in range(n, m+1):
				grams = ngrams(list(dna_string), N)
				# temp = []
				for gram in grams:
					# append tuple to temp array cuz ngram output tuple type
					# append keep the tuple in group of tuples
					# temp.append(gram)
					features.write(''.join(str(s) for s in gram) + '\n')
				# extend temp list to an array of tuple (all_grams)
				# all_grams.extend(temp)
			# motifs.write('//\n')
			features.write('//' + '\n')
			print(number)

	# create distinct motifs (features)
	# distinct_grams = set(all_grams)

	# count_dna = 0
	# motifs_most = []
	# print(len(temp_dna)/3)
	# # 70% occurence
	# for gram in distinct_grams:
	# 	count_dna = 0
	# 	str_gram = ''.join(gram)
	# 	for dna_s in temp_dna:
	# 		if str_gram in str(dna_s):
	# 			count_dna += 1
	# 			if count_dna > len(temp_dna)*7/10:
	# 				motifs_most.append(str_gram)
	# 				break
	# 	if len(motifs_most) >= 500:
	# 		break

	# for gram in motifs_most:
	# 	features.write(gram + '\n')

	# in the end print the number of sequence and gram 
	print(str(number) + ' sequences')
	# print(str(len(motifs_most)) + 'features')

	fyle.close()
	dna.close()
	features.close()

if __name__ == "__main__":
   main(sys.argv[1:])
