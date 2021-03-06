import json

try:
	data = {}
	data['protein'] =[]

	fp = open("../DATA/mud-crab-virus.fasta")
	line = fp.readline()
	cnt = 1
	while line:
		if ">" in line:
			data['protein'].append({
				'id': line
			})
			print(cnt, ": ", line)
			cnt += 1
		line = fp.readline()
finally:

	with open('Protein-Data.json', 'w') as outfile:
		json.dump(data, outfile);

	fp.close()