import math

n = 0

while True:
	n += 1
	triNum = ((n)*(n+1))/2
	triNumRt = math.floor(math.sqrt(triNum))
	count = 0

	if (triNumRt < 250):
		continue

	# count the divisors of triNum
	for i in range(2,triNumRt):
		if float(triNum)/i == math.floor(triNum/i):
			count +=2

	# Add 2 for 1 and the number itself
 	count += 2

	print count
	
	if (count > 500):
		print triNum
		print n
		break
