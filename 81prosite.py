# 81 prosite by Aman Panigrahi
# Co-Authors: Aman, Ashley
import mcb185
import sys
import re

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)

pat = '(C.{2,3}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	m = re.search(pat, seq)
	if m: print(m.group(1))