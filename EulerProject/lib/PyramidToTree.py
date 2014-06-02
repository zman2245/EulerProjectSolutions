from TreeNodeNumber import TreeNodeNumber
from ArrayOperations import numArrayToNodeArray
from ArrayOperations import strArrayToNumArray

# Assume a file with an upside-down pyramid format
# i.e. the root node is on the last line
def PyramidToTree(filename):
	file = open(filename, "r")
	line = file.readline()
	nodes = []

	if (not line):
		return None

	nums = strArrayToNumArray(line.split())
	nodes = numArrayToNodeArray(nums)
	line = file.readline()
	
	while line:
		nums = strArrayToNumArray(line.split())
		nodesNext = numArrayToNodeArray(nums)
		for i in range(len(nodesNext)):
			nodesNext[i].leftChild 	= nodes[i]
			nodesNext[i].rightChild = nodes[i+1]
			nodesNext[i].maxSum += max(nodes[i].maxSum, nodes[i+1].maxSum)

		nodes = nodesNext
		line = file.readline()

	return nodes[0]
