""" 
Binary tree from string
"""
s = "(1,2,3,4,5)"

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def string_to_tree(self,s):
        def build_tree(s, i):
            start = i
            if s[i] == '-': 
                i += 1
            while i < len(s) and s[i].isdigit(): 
                i += 1
            node = Node(int(s[start:i]))
            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = build_tree(s, i)
                i += 1
            if i < len(s) and s[i] == ')':
                i += 1
                node.right, i = build_tree(s, i)
                i += 1
            return node, i
        return build_tree(s, 0)[0] if s else None

tree = Tree()
tree.string_to_tree(s)
# print(tree.string_to_tree(s))