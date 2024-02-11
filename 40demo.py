import random
"""
for i in range(3):
	print()
	for j in range(random.randint(50, 60)):
		print(random.choice('ACGT'), end=(''))
nts = 'ACGT'

fo nt1 in nts:
		for nt2 in nts:
			if nt2 > nt1:
nts = 'ACGT'
limit = 4
len(x) # length of whatever is assigned a number
# Homework 34 solution
def = printmatrix(nts):
	limit = len(nts)
	for nt1 in nts:
		print(nt1, end= ' ')
	print()
	for i in range(0, limit):
		for j in range(0, limit):
			if i == j: print('+', end=' ')
			else: print('-', end=' ')
		print()
"""
win = 0
fail = 0
total = 0
for i in range(1000):
	d = random.randint(1, 20)
	total += 1
	if d >=10: win += 1
	else: fail += 1
print(win/total, fail/total, end=' ')
