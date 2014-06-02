from PyramidToTree import PyramidToTree
from TreeNodeNumber import TreeNodeNumber

rootNode = PyramidToTree("data_files/problem67_numberpyramid.txt")

# The tree builder populates maxSum for us!
print rootNode.maxSum
