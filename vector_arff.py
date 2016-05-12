import time
import sys, getopt

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def main(argv):
	mt = ''
	ft = ''
	vt = ''
	try:
		opts, args = getopt.getopt(argv,"hv:d:a:",["vector=","arff="])
	except getopt.GetoptError as e:
		print('vector.py -v <vector_file> -a <arff>')
		print(e)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('vector.py -v <vector_file> -a <arff>')
			sys.exit()
		elif opt in ("-a", "--vector"):
			ar = arg
		elif opt in ("-d", "--data"):
			dt = arg
		elif opt in ("-v", "--arff"):
			vt = arg
	print('Vector file is "', vt)
	print('subgenotype "', dt)
	print('arff file is "', ar)

	start_time = time.time()

	vector_file = open(vt, 'r')
	data_file = open(dt, 'r')
	arff_file = open(ar, 'w')
	# delete file content before writing
	deleteContent(arff_file)
	# read file
	data = data_file.read()
	vector_string = vector_file.read()
	dna_set = data.split("//\n")
	vector_set = vector_string.split("//\n")
	atr = []
	number = 0

	arff_file.write('@RELATION dna \n\n')
	
	for motifs_set in vector_set[0].split('\n'):
		if len(motifs_set) > 14:
			motifs = motifs_set.split()
			arff_file.write('@ATTRIBUTE ' + motifs[0].replace(">","") + ' NUMERIC\n')

	arff_file.write('@ATTRIBUTE class {A1, A2, A5, B1, B2, C1, C2, C4, D1, D2, D3, D4, D5, F1, F4}\n\n')
	
	# data
	arff_file.write('@data\n')

	for v in vector_set:
		vector = v.split('\n')
		iter_vector = iter(vector)
		next(iter_vector)
		for feature in iter_vector:
			if len(feature) > 5 and '>' not in feature:
				arff_file.write(feature.split()[1] + ',')
		for dna in dna_set:
			if vector[0] == dna.split('\n')[0] and len(dna) > 1:
				# print("vector 0 ", vector[0])
				# print("dna ", dna.split('\n')[1])
				# print(dna.split('\n')[1])
				arff_file.write(dna.split('\n')[1] + '\n')
	# end of file

	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   main(sys.argv[1:])