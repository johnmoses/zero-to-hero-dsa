""" 
Binary Tree with dfs and search
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root):
        self.root = root

    def dfs(self, node):
        print(node.data)
        for child in node.children:
            self.dfs(child)

    def search(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            result = self.search(data, child)
            if result:
                return result
        return None

a = Node("A")
b = Node("B")
c = Node("C")

a.add_child(b)
a.add_child(c)

# Let a be the root
tree = Tree(a)
tree.dfs(a)
tree.search('B',a)