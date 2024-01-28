# 23.hydropathy by Aman Panigrahi
# co-authors Aman, Adele
import math
import sys

def kytehydro(aa):
	if aa == 'A': return -1.8
	elif aa == 'C': return 2.50
	elif aa == 'D' or 'E' or 'N' or 'Q': return -3.50
	elif aa == 'F': return -2.50
	elif aa == 'G': return -0.4
	elif aa == 'H': return -3.20
	elif aa == 'I': return 4.5
	elif aa == 'K': return -3.90
	elif aa == 'L': return 3.80
	elif aa == 'M': return 1.9
	elif aa == 'P': return -1.60
	elif aa == 'R': return -4.50
	elif aa == 'S': return -0.80
	elif aa == 'T': return -0.70
	elif aa == 'V': return 4.20
	elif aa == 'W': return -0.90
	elif aa == 'Y': return -1.30
	else: return 'unknown amino acid'
print(kytehydro('B'))
print(kytehydro('E'))
print(kytehydro('T'))