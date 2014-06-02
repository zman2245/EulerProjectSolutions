def f(n):
	if n == 1:
		return 2

	val = f(n-1)
	return 2*val + val

print f(1)
print f(2)
print f(3)
print f(4)
print f(20)
