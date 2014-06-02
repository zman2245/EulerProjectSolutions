def f(n):
	if n == 1:
		return 1

	if n%2 == 0:
		return f(n/2) + 1
	else:
		return f(3*n + 1) + 1

max_count, max_i = 0, 0

for i in range(1, 999999):
	count = f(i)
	print i
	if count > max_count:
		max_count = count
		max = i

print max
