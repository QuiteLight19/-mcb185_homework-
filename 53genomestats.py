#53 genome stats by Aman Panigrahi
# Co-Authors: Aman, Ashley
import gzip
import sys
import math

path = sys.argv[1]
feature = sys.argv[2]

with gzip.open(path, 'rt') as data:
	length = []
	for line in data:
		words = line.split()
		if words[2] != feature: continue
		length.append(int(words[4]) - int(words[3]) + 1)

totall = 0
for n in length:
	totall +=n
	
length.sort()
count = len(length)
min = length[0]
max = length[-1]
mean = totall/count
if len(length) % 2 == 0:
	med1 = length[len(length)//2]
	med2 = length[len(length)//2 - 1]
	med  = (med1 + med2) / 2
else: med = length[len(length)//2]

sd = 0
for n in length:
	sd += ((mean - n)**2 / count)
sd = math.sqrt(sd)

print(count, min, max, int(mean), int(sd), int(med))
