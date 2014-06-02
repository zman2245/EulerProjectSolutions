from GridParse import fileTo2DArray

max = 0

M = fileTo2DArray("data_files/problem11_grid.dat")

print M[0][0] * M[0+1][0]
print M

rows = len(M)

for i in range(rows-3):
	cols = len(M[i])
	for j in range(cols-3):
		prod = M[i][j] * M[i][j+1] * M[i][j+2] * M[i][j+3] > max
		if (prod > max):
			max = prod

for i in range(rows-3):
	cols = len(M[i])
	for j in range(cols):
		if (j < 3):
			 continue
		prod = M[i][j] * M[i+1][j-1] * M[i+2][j-2] * M[i+3][j-3]
		if (prod > max):
			max = prod

for i in range(rows-3):
	cols = len(M[i])
	for j in range(cols-3):
		prod = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i+3][j+3]
		if (prod > max):
			max = prod

for i in range(rows-3):
	cols = len(M[i])
	for j in range(cols):
		prod = M[i][j] * M[i+1][j] * M[i+2][j] * M[i+3][j] > max
		if (prod > max):
			max = prod

print max
