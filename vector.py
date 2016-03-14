def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

motifs_file = open("data/motifs.gb", 'r')
features_file = open("data/features.gb", 'r')
vector_file = open("data/vector.gb", 'w')
# delete file content before writing
deleteContent(vector_file)
# read file
motifs_data = motifs_file.read()
features_data = features_file.read()
# data -> list of motifs
motifs_data = motifs_data.strip()
motifs_set_all = motifs_data.split('//')
features = features_data.split()

# each sequence
for motifs_set in motifs_set_all:
	if motifs_set != '':
		motifs = motifs_set.split()
		vector_file.write(motifs[0] + '\n')
		for feature in features:
			rate = motifs.count(feature)
			vector_file.write(feature + " " + str(rate) + '\n')
