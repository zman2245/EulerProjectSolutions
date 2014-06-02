import math
from PrimeNumbers import isPrime

x = 600851475143

n = math.sqrt(x)
i = math.floor(n)

while (i > 1):
	if x/i == math.floor(x/i):
		if isPrime(int(i)):
			print i
			break
	i -= 1

print "Done"
