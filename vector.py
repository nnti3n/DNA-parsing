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
		opts, args = getopt.getopt(argv,"hm:f:v:",["motifs=","features=","vector="])
	except getopt.GetoptError as e:
		print('vector.py -m <motifs_file> -f <features_file> -v <vector_file>')
		print(e)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('vector.py -m <motifs_file> -f <features_file> -v <vector_file>')
			sys.exit()
		elif opt in ("-m", "--motifs"):
			mt = arg
		elif opt in ("-f", "--features"):
			ft = arg
		elif opt in ("-v", "--vector"):
			vt = arg
	print('Motifs file is "', mt)
	print('Features file is "', ft)
	print('Vector file is "', vt)

	start_time = time.time()

	motifs_file = open(mt, 'r')
	features_file = open(ft, 'r')
	vector_file = open(vt, 'w')
	# delete file content before writing
	deleteContent(vector_file)
	# read file
	motifs_data = motifs_file.read()
	features_data = features_file.read()
	# data -> list of motifs
	motifs_data = motifs_data.strip()
	motifs_set_all = motifs_data.split('//')
	features = features_data.split()

	rates = []
	# each sequence
	for motifs_set in motifs_set_all:
		if motifs_set != '':
			motifs = motifs_set.split()
			rates.append(">" + motifs[0] + '\n')
			for feature in features:
				rate = motifs.count(feature)
				rates.append(feature + " " + str(rate) + '\n')
			rates.append('//\n')

	for line in rates:
		vector_file.write(line)

	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   main(sys.argv[1:])