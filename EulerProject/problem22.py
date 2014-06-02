file = open("data_files/problem22_names.txt")

line = file.readline()
linenum = 1
total_score = 0

while (line):
	score = 0
	for letter in line:
		if (letter == ' ') or (letter == '\n') or (letter == '\"'):
			continue
		score += (ord(letter) - 64)

	total_score += (score * linenum)
		
	linenum += 1
	line = file.readline()

print total_score
