# Red-Black Tree Node Example (Partial Implementation)

# Red-Black Tree Implementation

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Helper function to print the tree structure
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * level + prefix + str(root.key))
        if root.left or root.right:
            print_tree(root.left, level + 4, "L-- ")
            print_tree(root.right, level + 4, "R-- ")

def left_rotate(root):
    """
    Left Rotation:
    
    Before:          A
                    / \
                   B   C
                      / \
                     D   E
    
    After:           C
                    / \
                   A   E
                  / \
                 B   D
    """
    print("\nPerforming LEFT rotation on node", root.key)
    
    # The right child becomes the new root
    new_root = root.right
    
    if not new_root:
        print("Cannot rotate left - no right child!")
        return root
    
    # The right child's left subtree becomes the original root's right subtree
    root.right = new_root.left
    
    # The original root becomes the left child of the new root
    new_root.left = root
    
    print("New root after rotation:", new_root.key)
    return new_root

def right_rotate(root):
    """
    Right Rotation:
    
    Before:          A
                    / \
                   B   C
                  / \
                 D   E
    
    After:           B
                    / \
                   D   A
                      / \
                     E   C
    """
    print("\nPerforming RIGHT rotation on node", root.key)
    
    # The left child becomes the new root
    new_root = root.left
    
    if not new_root:
        print("Cannot rotate right - no left child!")
        return root
    
    # The left child's right subtree becomes the original root's left subtree
    root.left = new_root.right
    
    # The original root becomes the right child of the new root
    new_root.right = root
    
    print("New root after rotation:", new_root.key)
    return new_root

# Example 1: Left Rotation
print("EXAMPLE 1: LEFT ROTATION")
print("------------------------")
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

print("Original Tree:")
print_tree(root)

root = left_rotate(root)

print("\nTree after left rotation:")
print_tree(root)

# Example 2: Right Rotation
print("\n\nEXAMPLE 2: RIGHT ROTATION")
print("-------------------------")
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

print("Original Tree:")
print_tree(root)

root = right_rotate(root)

print("\nTree after right rotation:")
print_tree(root)

# Example 3: Double Rotation (Left-Right)
print("\n\nEXAMPLE 3: LEFT-RIGHT ROTATION")
print("-----------------------------")
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.right = TreeNode(15)

print("Original Tree:")
print_tree(root)

# First, left rotate the left child
root.left = left_rotate(root.left)
print("\nAfter left rotation of node 10:")
print_tree(root)

# Then, right rotate the root
root = right_rotate(root)
print("\nAfter right rotation of node 20:")
print_tree(root)

print("\n\nSUMMARY OF TREE ROTATIONS")
print("-------------------------")
print("1. Left Rotation: Used when right side is heavier")
print("2. Right Rotation: Used when left side is heavier")
print("3. Left-Right Rotation: First left rotate child, then right rotate parent")
print("4. Right-Left Rotation: First right rotate child, then left rotate parent")
print("\nRotations maintain the binary search tree property while rebalancing the tree.")

# Full implementation includes insertion, deletion, rotations, and fixups
# This snippet defines the node and color properties as a starting point.
