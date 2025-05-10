""" 
Find all paths from the root to leaves in a binary tree.

Example:
Input: root = [1, 2, 3, null, 5]
Output: ["1->2->5", "1->3"]

Explanation:
Use recursion or a stack to traverse each path from the root to the leaves.
Record each path as you traverse.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root):
    paths = []
    if not root:
        return paths
        
    def dfs(node, curr_path):
        if not node.left and not node.right:
            paths.append('->'.join(map(str, curr_path)))
            return
            
        if node.left:
            dfs(node.left, curr_path + [node.left.val])
        if node.right:
            dfs(node.right, curr_path + [node.right.val])
            
    dfs(root, [root.val])
    return paths

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)

# print(find_paths(root))

print(find_paths(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))))