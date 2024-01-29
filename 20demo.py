# 20demo.py by Aman Panigrahi

import math

def pythagoras(a, b):
	if a <= 0: exit('error: a must be greater than 0')
	if b <= 0: exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
print(pythagoras(1, 1))

def signflip(a): # flips the sign + > - and - > +
	return a * (-1)
print(signflip(-324))

def arearectangle(a, b): #length x width
	return a * b
print(arearectangle(4, 5))

def areacircle(a): #radius
	return round(a**2 * math.pi, 3)
print(areacircle(2))

def ctok(a): #Celsius to Kelvin
	return a + 273.15
print(ctok(25))

def mphtokph(a): #miles to kilometers
	return a * 1.609
print(mphtokph(24))

def midpoint(x1, y1, x2, y2):
	return((y2 - y1) / (x2-x1))
	return mx, my
print(midpoint(9, 9, 5, 4))

s = "hello world"
print(s, type(s))

a = 4
b = 3
if a == b:
	print('a equals b')
print(a, b)

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

def isinteger(a):
	c = (a % 2)
	if c == 0: return('even')
	elif c != 0: return('odd')
	else: return('unknown')
print(isinteger(1))

def isprobable(a): # numbers b/t 0 and 1, anything higher/lower is invalid.
	if a > 0 and a < 1: return('yessir')
	else: return('nah fam')
print(isprobable(0.5))

def nucleocomp(nt):
	if nt == 'A': return T
	elif nt == 'T': return A
	elif nt == 'C': return G
	elif nt == 'G': return C
	else: return unknown
print(nucleocomp('A'))

def nucleoweight(nt):
	if nt == A: return 313.21
	elif nt == T: return 304.2 D
	elif nt == C: return 289.18 D
	elif nt == G: return 329.21 D
	else: return wtf are you doing
print(nucleoweight('T'))
	
	
	
