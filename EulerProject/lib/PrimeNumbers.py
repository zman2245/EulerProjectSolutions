import math

# Useful functions for dealing with Prime Numbers, divisors, and such

def isPrime(x):
	"Returns True if x is prime, else returns False"

	# Special case 2
	if x == 2:
		return True

	maxFactor = math.sqrt(x)
	if maxFactor == math.floor(maxFactor):
		return False
	else:
		maxFactor = math.floor(maxFactor)

	if (x / 2.0) == (x / 2):
		return False

	b = 3.0
	while b <= maxFactor:
		if (x / b) == math.floor(x/b):
			return False
		b += 2

	return True

def isDivisor(n, x):
	"Returns True if x is a divisor of n, else returns False"
	if (float(n)/x == math.floor(float(n)/x)):
		return True

	return False

class PrimeNumberGenerator:
	def __init__(self):
		self.i = 2

	def getCurrentVal(self):
		return self.i

	def inc(self):
		tmp = self.i + 1
		while isPrime(tmp) == False:
			tmp += 1
		self.i = tmp
