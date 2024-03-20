# 61 skewer by Aman Panigrahi
#Co-Authors: Aman, Ashley
import biofun

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, biofun.gc_comp(s), dogma.gcskew(s))