# 22.oligotemp by Aman Panigrahi
#Co authors Aman, Ashley

import math

def oligotemp(a, c, g, t):
	total = (a + c + g + t)
	if type(a) != int or type(c) != int or type (g) != int or type(t) != int:
		return 'error: must be whole numbers'
	elif a < 0 or c < 0 or g < 0 or t < 0:
		return 'error: cannot have a negative amount of nucleotides'
	elif total <= 0 : return 'total has to be greater than 0'
	elif total <= 13: return ((a + t) * 2 + (g + c) * 4)
	elif total >  13: return (64.9 + (41 * (g + c - 16.4) / (a + c + g + t)))
	else			: return 'not possible'
print(oligotemp(-0.1, -1, -1, -1))
print(oligotemp(10, 10, 10, 10))
print(oligotemp(23, 45, 1, 3))
print(oligotemp(-11, 1, 1, 1))