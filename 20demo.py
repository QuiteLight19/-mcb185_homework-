# 20demo.py by Aman Panigrahi

import math

def pythagoras(a, b):
    if a <= 0: exit('error: a must be greater than 0') # needs to be exit, NOT sys.exit
    if b <= 0: exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
print(pythagoras(1, 1))

def signflip(a): # flips the sign (+ > - and - > +)  
	return (a * (-1))
print(signflip(-324))

def arearectangle(a, b): #length x width
	return (a * b)
print(arearectangle(4, 5))

def areacircle(a): #radius
	return round(a**2 * math.pi, 3)
print(areacircle(2))

def ctok(a): #Celsius to Kelvin
	return (a + 273.15)
print(ctok(25))

def mphtokph(a): #miles to kilometers
	return (a * 1.609)
print(mphtokph(24))

def midpoint (x1, y1, x2, y2):
	return((y2 - y1) / (x2-x1))
	return mx, my
print (midpoint(9, 9, 5, 4))

s = "hello world"
print(s, type(s))

a = 4
b = 3
if a == b:
	print ('a equals b')
print (a, b)

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print ('a == b')
# if a has remainder, print odd. no remainder, print even.

def isinteger(a):
	c = (a % 2)
	if c == 0: print ('even')
	elif c != 0: print ('odd')
	else: print ('unknown')
print(isinteger(1))
