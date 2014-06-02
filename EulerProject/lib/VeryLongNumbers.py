def fileToNumberStringList(filename):
	file = open(filename, "r")
 	line = file.readline()
  	idx = 0
	a = []

   	while line:
		a.append(line)
		line = file.readline()

	return a
