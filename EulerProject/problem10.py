from PrimeNumbers import PrimeNumberGenerator

primeNum = PrimeNumberGenerator()
sum = 0

while primeNum.getCurrentVal() < 2000000:
	sum += primeNum.getCurrentVal()
	primeNum.inc()
	print primeNum.getCurrentVal()

print sum
