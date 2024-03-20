#61 is recalculate
#62 is drop a letter, gain a letter


import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if   nt == 'A': A += 1
	elif nt == 'C': C += 1
	elif nt == 'G': G += 1
	elif nt == 'T': T += 1
	else: N +=1
print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq))