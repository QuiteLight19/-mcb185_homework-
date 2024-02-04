# 30 demo by Aman Panigrahi
"""
while True:
	print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3): #start, stop, interval
	print(i)

for i in range(5):
	print(i)

for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else		 : print(nt1, nt2, '-1')
	
limit = 4 # all possible unique pairings:
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
def tri(n):
	tri = 0
	for i in range(n+1):
		tri = i + tri
	return tri
print(tri(5))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / math.factorial(n)
		print(e)
	return e
print(euler(10))

import math
def isperfect_square(n):
	root = math.sqrt(n)
	if root == root // 1: return True
	return False
print(isperfect_square(5))

def is_prime(n):
	for den in range(2, n //2):
		if n % den == 0: return False
	return True
"""