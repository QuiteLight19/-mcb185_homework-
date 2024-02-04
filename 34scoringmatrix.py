# 34 scoring matrix by Aman Panigrahi
#Co-Authors Aman, 

seq= 'ACGT'
for nt in seq:
	print('', nt, end=' ')
print(' ')
for nt1 in seq:
	print(nt1, end=' ')
	for nt2 in seq:
		if nt1 == nt2: print('+1', end=' ')
		else: print('-1', end=' ')
	print()

