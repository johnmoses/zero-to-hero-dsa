# Tree Serialization - Python Example

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    def helper(node):
        if node is None:
            return "#,"
        return str(node.val) + "," + helper(node.left) + helper(node.right)
    return helper(root)

def deserialize(data):
    values = iter(data.split(','))
    
    def helper():
        val = next(values)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    return helper()

# Usage example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialized = serialize(root)
print("Serialized tree:", serialized)
new_root = deserialize(serialized)
print("Deserialized root value:", new_root.val)
