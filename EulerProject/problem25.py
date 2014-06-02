from FibIterator import FibonacciIterator

fib = FibonacciIterator()

while True:
	val = str(fib.getCurrentVal())
	if len(val) >= 1000:
		break
	fib.inc()

print fib.getCurrentTermNum()
