""" 
BST Search
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, node, target):
        if node is None:
            return None 
        elif node.data == target:
            return node
        elif target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)


a = Node("A")   # Root
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

tree = Tree(a)

# Search a node
print(tree.search(a, "G"))
