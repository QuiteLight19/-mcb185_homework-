# 22.oligotemp by Aman Panigrahi
#Co authors Aman, Ashley

import math

def oligotemp(a, c, g, t):
	total = (a + c + g + t)
	if total <= 13: return ((a + t)* 2) + ((g + c)* 4)
	elif total > 13: return (64.9 + 41* ((g+c - 16.4) / (total)))
print(oligotemp(10, 10, 10, 10))
print(oligotemp(23, 45, 1, 3))
print(oligotemp(1, 1, 1, 1))