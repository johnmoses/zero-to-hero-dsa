""" 
Tries

Basic representation
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

def insert(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]

    # Mark the end of the word
    curr.endOfWord = True

def search(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        if c not in curr.children:
            return False
        curr = curr.children[c]

    # Return true if the word exists and is marked as ending
    return curr.endOfWord

def isPrefix(root, key):
    curr = root
    for c in key:
        if c not in curr.children:
            return False
        curr = curr.children[c]

    return True

def delete(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        curr = curr.children[index]

    curr.endOfWord = False

root = TrieNode()
insert(root, "apple")
print(search(root, "apple"))
print(search(root, "app"))
print(isPrefix(root, "app"))
insert(root, "app")
print(search(root, "app"))
