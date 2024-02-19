#50 demo
import sys

"""
seq = 'GAATTC'
print(seq[0], seq[1])

for i in range(len(seq)):
	print(i, seq[i])

s = 'QWERTYUIOP'
print(s)

tax = ('Homo', 'sapiens', 9606)
print(tax[0])
print(tax[::-1])

nts = 'ACGTN'
for i, nt in enumerate(nts):
	print(i, nt)

nts = 'ACGTN'
names = 'adenosine', 'cytosine', 'guanine', 'thymine'
for nt, name in zip(nts, names):
	print(nt, name)

nts = ['A', 'T', 'C']

print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)
"""
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
"""
print(alph)
aas = list(alph)
print(aas)

vals = [1, 5, 8, 19, 2, 0.78, -3]
def mini(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
print(mini(vals), minmax(vals), mean(vals))

aas = list(alph)
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
"""
val = [len(val)//2]