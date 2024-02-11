# 43randomdna by Aman Panigrahi
# Co-Authors: Aman, Ashley
import random

a = 3
nts = 'ACGT'
for i in range(a):
	print(f'>seq-{i+1}')
	for j in range(random.randint(50, 60)):
		print(random.choice(nts), end='')
	print()