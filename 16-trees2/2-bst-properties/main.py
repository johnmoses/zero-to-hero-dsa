# BST Property Check - Python Example

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (is_bst(root.left, min_val, root.data) and
            is_bst(root.right, root.data, max_val))

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)

print("Is BST:", is_bst(root))
