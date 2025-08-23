# Recursive Tree Algorithms - Python Example

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(node):
    if node is None:
        return 0
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return max(left_height, right_height) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Tree height:", tree_height(root))
