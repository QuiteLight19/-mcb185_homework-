# 42chicago by Aman Panigrahi
import random

zerogames = 0
games = 1000
tscore = 0

for i in range(games):
	score = 0
	for rn in range(2, 13):
		d2 = random.randint(1, 6)
		d1 = random.randint(1, 6)
		if d1 + d2 == rn: score += rn
	tscore += score
	if score == 0: zerogames += 1
print(f' games with 0 pts is {zerogames / games}')
print(f' avg pts per game is {tscore/games}')
