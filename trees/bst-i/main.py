""" 
Binary Search Tree (BST) Example
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

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

    def search(self, node, target):
        if node is None:
            return None 
        elif node.value == target:
            return node
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

class Tree1:
    def __init__(self, root):
        self.root = root
    
    def pre_order(self, node):
        if node:
            print(node, end="")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node, end="")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node, end="")

    def search(self, node, target):
        if node is None:
            return None
        elif node.value == target:
            return node
        elif target < node.value:
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

# Let a be the root
tree = Tree1(a)

print("Preorder Traversal")
tree.pre_order(a)
print("\n")

print("Inorder Traversal")
tree.in_order(a)
print("\n")

print("Postorder Traversal")
tree.post_order(a)
print('\n ')

print('Search: ', tree.search(a, "G"))
