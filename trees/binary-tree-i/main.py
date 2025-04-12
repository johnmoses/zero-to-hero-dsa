""" 
Binary Tree with in-order traversal
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=" ")
        self.in_order(node.right)


# Create an instance of the tree
tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print("In-order traversal: ", end="")
tree.in_order(tree.root)
print()
