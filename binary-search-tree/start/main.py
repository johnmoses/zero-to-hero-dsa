""" 
Design a binary search tree with traversal functionality.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    
    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)


    def inorder(self):
        return self._inorder_recursive(self.root)


    def _inorder_recursive(self, node):
        if not node:
            return []
        return (self._inorder_recursive(node.left) + 
                [node.data] + 
                self._inorder_recursive(node.right))


    def preorder(self):
        return self._preorder_recursive(self.root)


    def _preorder_recursive(self, node):
        if not node:
            return []
        return ([node.data] + 
                self._preorder_recursive(node.left) + 
                self._preorder_recursive(node.right))


    def postorder(self):
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if not node:
            return []
        return (self._postorder_recursive(node.left) + 
                self._postorder_recursive(node.right) + 
                [node.data])

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Inorder traversal:", bst.inorder())
    print("Preorder traversal:", bst.preorder())
    print("Postorder traversal:", bst.postorder())
