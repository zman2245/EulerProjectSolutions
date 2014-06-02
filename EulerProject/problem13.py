from VeryLongNumbers import fileToNumberStringList

# Start at beginning digits, add them up. Multiply by 10 and add the to the sum of the next digits.

M = fileToNumberStringList("data_files/problem13_numbers.dat")

rows = len(M)
cols = len(M[0])

sum = 0
pos = 0

for pos in range(cols):
	for i in range(rows):
		sum += int(M[i][pos])

	sum *= 10
	
	print sum
