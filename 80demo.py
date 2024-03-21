import sys
import gzip
import json
import mcb185

introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		print(f[2])
		if f[2] != 'intron': continue
		chrom = f[0]
		beg = int(f[3]) -1
		end = int(f[4]) -1
		strand = f[6]
		n = int(f[5])
		introns.append((chrom, beg, end, strand, n))
#print('introns:', len(introns))

dons = []
accs = []
dlen = 6
aclen = 8
for i in range(dlen):
	dons.append({'A':0, 'C':0, 'G':0, "T":0})
for i in range(aclen):
	accs.append({'A':0, 'C':0, 'G':0, "T":0})
#print(json.dumps(dons, indent = 4))

for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for chrom, beg, end, strand, n in introns:
		print(chrom, beg, end)
		for c, b, e, s, n in introns:
			if chrom == c and s== '+':
				iseq = seq[b:e+1]
				if s == '-': iseq = mcb185.anti_seq(iseq)
				don = iseq[:6]
				for i, nt in enumerate(don):
					dons[i][nt] +=1
				acc = iseq[-8:]
				for i, nt in enumerate(acc):
					accs[i][nt] +=1
for i, counts in enumerate(accs):
	a = n['A']
	c = n['C']
	g = n['G']
	t = n['T']
	#print(i+1, n['A'], n['C'], n['G'], n['T'])

"""
		#introns.append((chrom, beg, end, strand, score))
		if chrom not in introns: introns[chrom] = []
		introns[chrom].append({
			'beg': beg,
			'end' : end,
			'strand' : strand,
			'count' : score})
print(json.dumps(introns, indent=4))
"""