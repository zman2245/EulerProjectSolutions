max = 5*(9**5)
totalSum = 0

for i in range (2,max+1):
	strVal = str(i)
	sum = 0
	for digit in strVal:
		sum += int(digit)**5
	
	if i == sum:
		totalSum += i

print totalSum
