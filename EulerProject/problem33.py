from fractions import Fraction

for num in range(10,20):
	for den in range(num, 20):
		numStr = str(num)
		denStr = str(den)

		numReduced = int(numStr[0])
		denReduced = int(denStr[1])

		if denReduced != 0:
			# This will automatically reduce the fraction
			x = Fraction(numReduced, denReduced)
		
			numStr = str(x.numerator) + numStr[1:]
			denStr = denStr[:1] + str(x.denominator)

			print numStr

			newNum = int(numStr)
			newDen = int(denStr)

			if (newNum * den) == (num * newDen):
				print num/den


		numStr = str(num)
		denStr = str(den)

		numReduced = int(numStr[1])
		denReduced = int(denStr[0])

		if denReduced != 0:
			# This will automatically reduce the fraction
			x = Fraction(numReduced, denReduced)
		
			numStr = numStr[:1] + str(x.numerator)
			denStr = str(x.denominator) + denStr[1:]

			newNum = int(numStr)
			newDen = int(denStr)

			if (newNum * den) == (num * newDen):
				print num,den

