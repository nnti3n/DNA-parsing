from nltk.util import ngrams

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def dna_filter(virus):
	dna = virus.split(mark, 1)[1].replace(" ", "").replace("\n", "")
	dna_filtered = ''.join(i for i in dna if not i.isdigit())
	return dna_filtered

char = "subtype: B2"
mark = "ORIGIN"
# N-Grams range
n = 5
m = 10
number = 0

# open file
fyle = open("data/hbv-genotype-c.gb")
dna = open("data/result.gb", 'w')
features = open("data/features.gb", 'w')
# delete file content before writing
deleteContent(dna)
deleteContent(features)
# read file into string
data = fyle.read()
# split data into sequences
sequences = data.split("//")

for sequence in sequences:
	if char in sequence:
		number += 1
		# print DNA to result.gb
		dna_string = dna_filter(sequence)
		dna.write(dna_string + '\n' + '//' + '\n')
		# exact into features and print to features.gb
		for N in range(n+1, m+1):
			grams = ngrams(list(dna_string), N)
			for gram in grams:
				features.write(' '.join(str(s) for s in gram) + '\n')
		features.write('//\n')


print(str(number) + ' sequences')

fyle.close()
dna.close()
features.close()
