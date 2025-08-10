""" 
Binary Search Tree (BST) Example
"""

class Node:
    """
    Node class for BST
    """
    def __init__(self, value):
        """
        Initialize a node with a value
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Return the value of the node as a string
        """
        return str(self.value)

class Tree:
    def __init__(self, root):
        """
        Initialize a tree with a root node
        """
        self.root = root

    def insert(self, node, value):
        """
        Insert a value into the tree
        Time Complexity: O(n)
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(node.right, value)

    def insert_values(self, values):
        """
        Insert lists, dictionaries and tuples into the tree
        """
        if isinstance(values, (list, tuple)):
            for value in values:
                self.insert(self.root, value)
        elif isinstance(values, dict):
            for key, value in values.items():
                self.insert(self.root, key)
                self.insert(self.root, value)

    def delete(self, value):
        """Public method to start deletion"""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """
        Delete a value from the tree
        """
        if node is None:
            return node
        # Find the node to delete by recursively traversing the tree
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node to delete found - handle the three cases
            
            # Case 1: Leaf node (no children)
            if not node.left and not node.right:
                return None
            
            # Case 2: Node has only one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 3: Node has two children
            # Find smallest value in right subtree
            current = node.right
            while current.left:
                current = current.left
            
            # Copy the value and delete the successor
            node.value = current.value
            node.right = self._delete(node.right, current.value)
        
        return node
        
    def pre_order(self, node):
        """
        Pre-order traversal of the tree
        """
        if node:
            print(node, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        """
        In-order traversal of the tree
        """
        if node:
            self.in_order(node.left)
            print(node, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        """
        Post-order traversal of the tree
        """
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node, end=" ")

    def search(self, node, target):
        """
        Search for a target value in the tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if node is None:
            return None 
        elif node.value == target:
            return node
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)
    
    def bfs(self, node, target):
        """
        Breadth-first search of the tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            if current_node.value == target:
                return current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return None

    def dfs(self, node, target):
        """
        Depth-first search of the tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [node]
        while stack:
            current_node = stack.pop()
            if current_node.value == target:
                return current_node
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return None


a = Node("A")   # Root
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

# Let a be the root
tree = Tree(a)

print("Insert")
tree.insert(a, "H")
tree.insert_values(["I", "J", "K", "L", "M"])
tree.insert_values({"Cloud": "AWS", "OS": "Linux", "Language": "Python"})

print("Preorder Traversal")
tree.pre_order(a)
print("\n")

print("Inorder Traversal")
tree.in_order(a)
print("\n")

print("Postorder Traversal")
tree.post_order(a)
print('\n ')

print('Search: ', tree.search(a, "G"))

print('BFS: ', tree.bfs(a, "G"))

print('DFS: ', tree.dfs(a, "G"))

print("Delete")
tree.delete("M")
tree.delete("L")

print("Preorder Traversal")
tree.pre_order(a)