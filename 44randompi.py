# 44 random pi by Aman Panigrahi
# Co-Authors: Aman, Ashley
import random
import math

inside = 0
runs = 0
while True:
	x = random.random()
	y = random.random()
	runs +=1
	if math.sqrt(x**2 + y**2) < 1.0:
		inside += 1
	pi = ((inside/runs)*4)
	print(pi)
"""
while True:
	x = random.random()
	y = random.random()
	runs += 1
	if math.sqrt(x**2 + y**2) < 1: inside +=1
	print(f'pi = {4*inside/runs}')
"""
	