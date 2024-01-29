# 24accuracy by Aman Panigrahi
import math

def f1scoreacc(a, b, c, d): # a = true +, b= false +, c is true - d is false -
	p = (a / (a+b))
	r = (a / (a+d))
	score = ((2 * p * r)/(p + r))
	accuracy = ((a+c) / (a+b+c+d))
	if   a > 1 or a < 0: return 'value must be between 0 and 1'
	elif b > 1 or b < 0: return 'value must be between 0 and 1'
	elif c > 1 or c < 0: return 'value must be between 0 and 1'
	elif d > 1 or d < 0: return 'value must be between 0 and 1'
	elif score > 1 or score < 0: return 'total must be between 0 and 1'
	return round(score, ndigits = 4), round(accuracy, ndigits = 4)
print(f1scoreacc(0.3, 0.3, 0.2, 0.1))
print(f1scoreacc(2.3, 0.4, 1, .13))
print(f1scoreacc(0.1, 0.1, 0.7, 0.7))
print(f1scoreacc(0.134, 0.9853, 0.3, 0.49))
print(f1scoreacc(-0.134, 0.56, 0.25, 0.99))

"""
precision: a/(a+b)
recall: a/(a+d)
"""