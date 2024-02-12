# 47deathsaves by Aman Panigrahi
#Co-Authors: Aman, Ashley
import random

die = 0
stable = 0
revive = 0
games = 1000

for i in range(games):
	f = 0
	s = 0
	r = 0
	while f < 3 and s < 3 and r < 1:
		d = random.randint(1, 20)
		if   d == 20: r += 1
		elif d <  20 and d >= 10: s += 1
		elif d <  10 and d >=  2: f += 1
		else					: f += 2
		if f >= 3				: die += 1
		if r == 1				: revive += 1
		if s == 3				: stable +=1

print(die/games)
print(stable/games)
print(revive/games)