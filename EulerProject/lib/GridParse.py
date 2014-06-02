def fileTo2DArray(filename):
	file = open(filename, "r")
 	line = file.readline()
  	idx = 0
	a = []

   	while line:
		a.append(line.split())
		line = file.readline()

	# convert strings to ints
	rows = len(a)
	for i in range(rows):
		cols = len(a[i])
		for j in range(cols):
			a[i][j] = int(a[i][j])

	return a
