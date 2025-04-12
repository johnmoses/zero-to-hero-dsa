""" 
Splay tree
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def new_node(key):
    return Node(key)

def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def splay(root, key):
    if root is None :
      return  new_node(key)
    if root.key == key:
        return root

    if root.key > key:
        if root.left is None:
            return root
        if root.left.key > key:
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)
        elif root.left.key < key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = left_rotate(root.left)
        return root.left if root.left is None else right_rotate(root)
    else:
        if root.right is None:
            return root
        if root.right.key > key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = right_rotate(root.right)
        elif root.right.key < key:
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)
        return root.right if root.right is None else left_rotate(root)

def insert(root, key):
    if root is None:
        return new_node(key)

    root = splay(root, key)

    if root.key == key:
        return root

    node = new_node(key)
    if root.key > key:
        node.right = root
        node.left = root.left
        root.left = None
    else:
        node.left = root
        node.right = root.right
        root.right = None
    return node

def pre_order(node):
    if node:
        print(node.key, end=" ")
        pre_order(node.left)
        pre_order(node.right)

if __name__ == "__main__":
    root = None
    root = insert(root, 100)
    root = insert(root, 50)
    root = insert(root, 200)
    root = insert(root, 40)
    root = insert(root, 60)
    print("Preorder traversal of the modified Splay tree:")
    pre_order(root)