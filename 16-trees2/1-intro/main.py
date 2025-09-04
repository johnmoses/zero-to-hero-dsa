# Basic BST Node - Python Example

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Simple insertion maintaining BST property
def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.data:  # Fixed: Compare with root.data instead of root
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

root = None
for val in [10, 5, 15, 3, 7, 13, 17]:
    root = insert(root, val)
print("BST constructed with root:", root.data)