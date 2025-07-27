""" 
Tries

An OOP approach
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def isPrefix(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.isPrefix("app"))
trie.insert("app")
print(trie.search("app"))
