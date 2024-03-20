# 73missing kmers by Aman Panigrahi
#Co-Authors: Aman, Ashley
import sys
import mcb185
import itertools

fasta = sys.argv[1]
for k in range(1, 10):
	kcount = {}
	for defline, seq in mcb185.read_fasta(fasta):
		rev = mcb185.anti_seq(seq)
		for i in range(len(seq) -k +1):
			kmer  = seq[i:i+k]
			rkmer = rev[i:i+k]
			if kmer  not in kcount: kcount[kmer]  = 0
			if rkmer not in kcount: kcount[rkmer] = 0
			kcount[kmer]  += 1
			kcount[rkmer] += 1
		if len(kcount.keys()) == 4**k: continue
		for ktup in itertools.product('ACGT', repeat=k):
			kmer = ''.join(ktup)
			if kmer not in kcount: print(kmer)
