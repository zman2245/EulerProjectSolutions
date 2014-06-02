from TreeNodeNumber import TreeNodeNumber

def numArrayToNodeArray(a):
	for i in range(len(a)):
		a[i] = TreeNodeNumber(a[i])

	return a

def strArrayToNumArray(a):
	for i in range(len(a)):
		a[i] = int(a[i])
	
	return a
