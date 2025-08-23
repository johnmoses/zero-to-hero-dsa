# Binary Tree Structure - Python Example

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_full_binary_tree(node):
    if node is None:
        return True
    if (node.left is None) != (node.right is None):
        return False
    return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Is full binary tree:", is_full_binary_tree(root))
