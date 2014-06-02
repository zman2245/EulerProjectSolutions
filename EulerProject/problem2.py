from FibIterator import FibonacciIterator

x = FibonacciIterator()
sum = 0

while (x.getCurrentVal() < 4000000):
	if (x.getCurrentVal() % 2) == 0:
		sum += x.getCurrentVal()

	x.inc()

print sum
