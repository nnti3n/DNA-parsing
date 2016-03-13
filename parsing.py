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
number = 0
n = 5
m = 10

# open file
fyle = open("data/hbv-genotype-c.gb")
dna = open("data/result.gb", 'w')
features = open("data/features.gb", 'w')
# delete file content before writing
deleteContent(dna)
deleteContent(features)
# read file into string
data = fyle.read()
# split data into viruses
viruses = data.split("//")

for virus in viruses:
	if char in virus:
		number += 1
		# print DNA to result.gb
		dna_string = dna_filter(virus)
		dna.write(dna_string + '\n' + '//' + '\n')
		# exact into features and print to features.gb
		for N in range(n, m):
			grams = ngrams(list(dna_string), N)
			for gram in grams:
				features.write(' '.join(str(s) for s in gram) + '\n')


print(str(number) + 'sequences')

fyle.close()
dna.close()
features.close()
