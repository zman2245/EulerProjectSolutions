# May need refactoring if I use similar trees
# elsewhere. Below, maxSum is the maximum sum
# of this node plus values in the path to any
# leaf

class TreeNodeNumber:

	def __init__(self, val):
		self.val 		= val
		self.maxSum		= val
		self.leftChild 	= None
		self.rightChild = None

