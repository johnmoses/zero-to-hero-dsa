"""
Binary Trees

Given some items, A, B, C, and so on, write a basic binary tree to demonstrate it's core functionalities
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

# Test
print("a.right.left.data:", a.right.left.data)

# Traverse
print('Traverse 1:')
tree = []
root = a
nodes = []
while root or nodes:
    while root:
        nodes.append(root)
        root = root.left
    root = nodes.pop()
    tree.append(root.data)
    root = root.right
values = [str(i) + '->' for i in tree]
print(values)

# Traverse tree
print('Traverse 2:')
def traverse(root):
    if root is None:
        return
    print(root.data, end=" -> ")
    traverse(root.left)
    traverse(root.right)

traverse(a)