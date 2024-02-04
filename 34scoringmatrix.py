# 34 scoring matrix by Aman Panigrahi
#Co-Authors Aman, 

seq= 'ACGT'
for nt in seq:
	print('', nt, end=' ')
print(' ')
for nt1 in seq:
	for nt2 in seq:
		if nt1 == nt2 and nt2 == 'A': print(nt1, '+1 -1 -1 -1')
		if nt1 == nt2 and nt2 == 'C': print(nt1, '-1 +1 -1 -1')
		if nt1 == nt2 and nt2 == 'G': print(nt1, '-1 -1 +1 -1')
		if nt1 == nt2 and nt2 == 'T': print(nt1, '-1 -1 -1 +1')

