# 25entropy by Aman Panigrahi
# co-authors: Aman, David
import math

def shannonentropy(a, c, g, t):	
	nt = (a + c + g + t)
	pa = (a / nt)
	pc = (c / nt)
	pg = (g / nt)
	pt = (t / nt)
	if type(a) != int or type(c) != int or type (g) != int or type(t) != int:
		return 'error: values must be integers'
	elif a < 0 or c < 0 or g < 0 or t < 0:
		return 'must be positive'
	else:
		return -(pa * math.log2(pa) + pc * math.log2(pc) + pg * math.log2(pg) + pt * math.log2(pt))
print(shannonentropy(1, 9, 2, 3))
print(shannonentropy(12, 452, 235, 134))
print(shannonentropy(-3, 4, 3, 98))