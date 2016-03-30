from nltk.util import ngrams

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def dna_filter(sequence):
	dna = sequence.split(dna_mark, 1)[1].replace(" ", "").replace("\n", "")
	dna_filtered = ''.join(i for i in dna if not i.isdigit())
	return dna_filtered

char = "subtype: B2"
dna_mark = "ORIGIN"
all_grams = []
# N-Grams range
n = 10
m = 30
number = 0

# open file
fyle = open("data/hbv-genotype-c.gb")
dna = open("data/result.gb", 'w')
motifs = open("data/motifs.gb", 'w')
features = open("data/features.gb", 'w')
# delete file content before writing
deleteContent(dna)
deleteContent(motifs)
# read file
data = fyle.read()
# split data into sequences
sequences = data.split("//")

for sequence in sequences:
	if char in sequence:
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
