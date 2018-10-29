from copy import copy
import math

paths = []
city_names = ["NY", "LA", "DEN"]
paths.append([8, 3, 10, 43, 15, 48, 5, 40, 20, 30, 28, 24])
paths.append([18, 1, 35, 18, 10, 19, 18, 10, 8, 5, 8, 20])
paths.append([40, 5, 8, 13, 21, 12, 4, 27, 25, 10, 5, 15])

# paths.append([8, 18, 40])
# paths.append([3, 1, 5])
# paths.append([10, 35, 8])
# paths.append([43, 18, 13])
# paths.append([15, 10, 21])
# paths.append([])

fixed_costs = [[0, 20, 15],
               [20, 0, 10],
               [15, 10, 0]]
treeLeaves = []

class nodeTree:
    def __init__(self, city=None, parent=None, value=0, depth=0):
        self.city = city
        self.parent = parent
        self.value = value
        self.children = []
        self.depth = depth

    def printNode(self):
        print(self.city, self.value, self.children)

    def addChildren(self, arr):
        treeLeaves.remove(self)
        for c, name in enumerate(city_names):
            child = nodeTree(name, self, self.value + arr[c] + fixed_costs[city_names.index(self.city)][c], self.depth + 1)
            self.children.append(child)
            treeLeaves.append(child)

    def initAddChildren(self, arr):
        for c, name in enumerate(city_names):
            child = nodeTree(name, self, arr[c], self.depth + 1)
            self.children.append(child)
            treeLeaves.append(child)

    def findMin(self):
        children = [child.value for child in self.children]
        return min(children)



def main():
    nodeMegaTree = []
    n0 = nodeTree()
    nodeMegaTree.append(n0)
    n0.initAddChildren([8, 18, 40])
    for newNode, w in enumerate(paths[0]):
        p = [paths[0][newNode], paths[1][newNode], paths[2][newNode]]
        leaves = copy(treeLeaves)
        for node in leaves:
            if node.depth == newNode:
                node.addChildren(p)

    minLeaf = None
    minimum = math.inf
    for leaf in treeLeaves:
        if leaf.value < minimum:
            minimum = leaf.value
            minLeaf = leaf

    tour = ""
    print(minLeaf.value)
    while minLeaf.depth != 0:
        tour = minLeaf.city + " " + tour
        minLeaf = minLeaf.parent

    print(tour)

main()
