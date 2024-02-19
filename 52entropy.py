# 52entropy by Aman Panigrahi
import sys
import math

probs = []
for arg in sys.argv[1:]:
	n = float(arg)
	assert(n > 0 and n < 1)
	probs.append(float(arg))

total = 0
for p in probs: total += p
if not math.isclose(total, 1.0): 
	sys.exit('total must add up to 1')

h = 0
for p in probs:
	h -= p * math.log2(p)
print(h)