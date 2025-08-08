"""
Binary Search Trees

Given some items, A, B, C, and so on, write a basic binary tree to demonstrate it's core functionalities
"""

class Node:
    def __init__(self, value):
        self.value = value
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

# Access values
print("a.right.left.value:", a.right.left.value)

# Traverse example
print('Traverse:')
def traverse(root):
    if root is None:
        return
    print(root.value, end=" -> ")
    traverse(root.left)
    traverse(root.right)

traverse(a)