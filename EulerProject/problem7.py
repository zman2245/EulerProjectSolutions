from PrimeNumbers import PrimeNumberGenerator

primeNum = PrimeNumberGenerator()

i = 1

while i < 10001:
	primeNum.inc()
	i += 1

print primeNum.getCurrentVal()
