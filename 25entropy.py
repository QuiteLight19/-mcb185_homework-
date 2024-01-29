# 25entropy by Aman Panigrahi
# co-authors: Aman, David, Ashley
import math

def shannonentropy(a, c, g, t):	
	nt = (a + c + g + t)
	pa = (a / nt)
	pc = (c / nt)
	pg = (g / nt)
	pt = (t / nt)
	entropy = 0
	if a > 0: entropy = entropy + pa*math.log2(pa)
	if c > 0: entropy = entropy + pc*math.log2(pc)
	if g > 0: entropy = entropy + pg*math.log2(pg)
	if t > 0: entropy = entropy + pt*math.log2(pt)
	return -entropy
print(shannonentropy(1, 9, 2, 3))
print(shannonentropy(12, 452, 235, 134))
print(shannonentropy(0, 4, 3, 98))