from PyramidToTree import PyramidToTree

root = PyramidToTree("data_files/problem18_numberpyramid.txt")

print root.maxSum
print root.val
print root.leftChild.val
print root.leftChild.rightChild.rightChild.val
