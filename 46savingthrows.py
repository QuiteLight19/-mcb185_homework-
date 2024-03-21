# 46 savningthrows
# Co-Authors: Aman, Ashley
import random

def normal():
	return random.randint(1, 20)

def advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2: return r1
	else	   : return r2

def disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 <= r2: return r1
	else	   : return r2


trials = 1000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = advantage()
		if rn >= dc: success += 1
	print(success/trials)

for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = normal()
		if rn >= dc: success += 1
	print(success/trials)
	
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		rn = disadvantage()
		if rn >= dc: success += 1
	print(success/trials)

"""
for dc in range(5, 16, 5):
	print(dc, end='\t')
	adv = 0
	dis = 0
	nor = 0
	for j in range(trials):
		if normal() >= dc: nor += 1
		if advantage() >= dc: adv += 1
		if disadvantage() >= dc: dis += 1
	print(nor/trials, dis/trials, adv/trials)
"""