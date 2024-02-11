# 45 dndstats by Aman Panigrahi
# Co-authors: Aman, Ashley
import random

trials = 10000
total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		score += random.randint(1, 6)
	total +=score
print(total/trials)

totalr1 = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d == 1: score += d2
		elif d >  1: score += d
	totalr1 +=score
print(totalr1/trials)

totalx2 = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: score += d1
		if d1 <  d2: score += d2
	totalx2 += score
print(totalx2/trials)

total4d1 = 0
for i in range(trials):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if   d1 <= d2 and d1 <= d3 and d1 <= d4: score = d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score = d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score = d1 + d2 + d4
	elif d4 <= d1 and d4 <= d2 and d4 <= d3: score = d1 + d2 + d3
	total4d1 += score
print(total4d1/trials)