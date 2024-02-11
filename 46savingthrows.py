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


trials = 100
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
		