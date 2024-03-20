# 64 profinder by Aman Panigrahi
# Co-Authors: Aman, Ashley

import sys
import mcb185
import biofun

def find_protein(aas, size):
	valid = []
	for orf in aas.split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= size:
				valid.append(protein)
	return valid

def process(seq, size):
	valid = []
	for i in range(3):
		aas = biofun.translate(seq[i:])
		for protein in find_protein(aas, size):
			valid.append(protein)
	rev_aas = biofun.revcomp(seq)
	for i in range(3):
		aas = biofun.translate(rev_aas[i:])
		for protein in find_protein(aas, size):
			valid.append(protein)
	return valid

size = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	proteins = process(seq, size)
	for i, protein in enumerate(proteins):
		id = f'{defline.split()[0]}-prot-{i+1}'
		print(f'>{id}\n{protein}')
