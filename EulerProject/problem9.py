import math

a = b = 1
isDone = False

while a < 1000:
	b = a
	while b < 1000:
		c = math.sqrt(a**2 + b**2)
		if (a+b+c > 1000):
			break

		if c == math.floor(c):
			if (a + b + c) == 1000:
				print a
				print b
				print c
				print a*b*c
				isDone = True
				break
		b += 1

	if (isDone == True):
		break
	a += 1

print "Done!"
