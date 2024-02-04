# 32fibonacci by Aman Panigrahi
# Co-Authors: Aman, 

import math
a = 0
b = 1

for i in range(10):
	c = a + b
	a = b
	b = c
	print(a)