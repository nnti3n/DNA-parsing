char = "subtype: B2"
dna = "ORIGIN"
number = 0

fyle = open("data/hbv-genotype-c.gb")
fyler = open("data/result.gb", 'r+')
data = fyle.read()
# fyler.write("DNA sequences of Hepatitis B Genotype B Subgenotype B2 \n")
viruses = data.split("//")

for virus in viruses:
	if char in virus:
		number += 1
		dna_string = virus.split(dna, 1)[1].replace(" ", "")
		dna_string_filtered = ''.join(i for i in dna_string if not i.isdigit())
		fyler.write(dna_string_filtered + '\n' + '//' + '\n')

# fyler.write(str(number) + 'sequences\n')
print(str(number) + 'sequences')

fyle.close()
fyler.close()
