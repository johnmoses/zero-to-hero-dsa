# Tree Node Definition - Python Example

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Root node:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
