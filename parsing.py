char = "subtype: B2"
dna = "ORIGIN"
number = 0

fyle = open("hbv-genotype-c.gb")
fyler = open("result.gb", 'w')
data = fyle.read()
fyler.write("DNA sequences of Hepatitis B Genotype B Subgenotype B2 \n")
viruses = data.split("//")

for virus in viruses:
	if char in virus:
		number += 1
		dna_string = virus.split(dna, 1)[1]
		fyler.write(dna_string + '\n' + '//' + '\n')

fyler.write(str(number) + 'sequences\n')
print(str(number) + 'sequences')

fyle.close()
fyler.close()
