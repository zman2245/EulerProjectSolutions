n = 1
val = n

while n < 100:
	val = val*n
	if (n % 10 == 0):
		val = val / 100
	n += 1	

val = val / 10000

valString = str(val)
sum = 0

for digit in valString:
	sum += int(digit)

print sum
