# Build the list
terms = {}

for a in range(2,101):
	for b in range(2,101):
		val = a**b
		terms[val] = val

print len(terms)
