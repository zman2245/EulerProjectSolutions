import math
from PrimeNumbers import isDivisor

def d(n):
	maxDivisor = math.sqrt(n)
	sum = 1 #include 1 for all numbers

	for i in range (2, int(maxDivisor+1)):
		if isDivisor(n, i):
			if i == (n/i):
				sum += i
			else:
				sum += (i + (n/i))
	
	return sum

sum = 0

for i in range(1,10000):
	val = d(i)
	if (i == d(val)) and (i != val):
		sum += i + val
		print val, i, sum
	
print sum
print sum/2
