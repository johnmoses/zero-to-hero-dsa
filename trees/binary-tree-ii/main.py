"""
Basic binary tree with pre-order, in-order and post-order traversals
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

    def pre_order(self, node):
        if node:
            print(node, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node, end=" ")

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

# Let a be the root
tree = Tree(a)

print("Preorder Traversal")
tree.pre_order(a)
print("\n")

print("Inorder Traversal")
tree.in_order(a)
print("\n")

print("Postorder Traversal")
tree.post_order(a)
