""" 
Depth First Search by recursion on a binary tree

Example 1:
    Input: root = [1, null, 2, 3]
    Output: [1, 2, 3]

Example 2:
    Input: root = []
    Output: []

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

def dfs1(root):
    if not root:
        return []
    return [root.val] + dfs1(root.left) + dfs1(root.right)

def dfs2(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

print(dfs1(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))
print(dfs2(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))