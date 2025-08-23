# Tree Rotations - Python Example

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

# Usage
root = TreeNode(10)
root.right = TreeNode(20)
root = left_rotate(root)
print("Root after left rotation:", root.key)
