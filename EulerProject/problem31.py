denoms = [1, 2, 5, 10, 20, 50, 100, 200]
maxTotal  = 200
leafCount = 0

class CoinNode:
    def __init__(self):
        self.children = []
        self.lineage  = []
        self.value    = 0
        self.total    = 0


def buildTree(node):
    global leafCount
    global maxTotal
    global denoms

    # base case: total of 1 (100%) is reached
    if node.total == maxTotal:
        leafCount += 1
        print leafCount
        node.lineage.append(node.value)
        #print node.total
        #print node.lineage
        return

    for denom in denoms:
        if denom > node.value:
            continue

        if node.total + denom > maxTotal:
            continue

        child = CoinNode()
        child.value = denom
        child.total = node.total + denom
        # commented out lineage for perf; comment back in for debug
        #child.lineage = node.lineage[:]
        #child.lineage.append(node.value)
        #depth first
        buildTree(child)


# build a tree for each possible start node
for denom in denoms:
    node = CoinNode()
    node.value = denom
    node.total = denom
    buildTree(node)

print leafCount
