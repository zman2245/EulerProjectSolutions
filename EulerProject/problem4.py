from PrimeNumbers import isPrime

def isPalindrome(x):
	xString = str(x)

	for i in range(0, len(xString)/2):
		if xString[i] != xString[len(xString)-i-1]:
			return False
	return True

maxPal = 0
i = 999

while i > 0:
	j = 999
	while j > i:
		prod = i*j
		if isPalindrome(prod):
			if prod > maxPal:
				maxPal = prod
		j -= 1
	i -= 1

print maxPal
