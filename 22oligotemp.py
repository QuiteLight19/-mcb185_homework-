""" 22.oligotemp by Aman Panigrahi
Oligo melting temperature given A T G C in sequence
<= 13 nt, Tm (A+T)*2 + (G+C)*4
longer than 13: 64.9 + 41*(G+C) - 16.4/ (A+T+G+C)
"""
import math

def oligotemp(a, c, g, t):
	total = (a+t+g+c)
	if total <= 13: return ((a + t)* 2) + ((g + c)* 4)
	elif total > 13: return (64.9 + 41* ((g+c - 16.4) / (total)))
print(oligotemp(10, 10, 10, 10))