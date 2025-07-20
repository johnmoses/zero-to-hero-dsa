""" 
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def find_all_words(self):
        result = []

        def dfs(node, path):
            if node.is_end_word:
                result.append(path)

            for char, child_node in node.children.items():
                dfs(child_node, path + char)

        dfs(self.root, "")
        return result


def find_words(board, words):
    # Build Trie
    trie = Trie()
    for word in words:
        trie.insert(word)

    m, n = len(board), len(board[0])
    result = set()

    def dfs(i, j, node, path):
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        char = board[i][j]
        if char not in node.children:
            return

        node = node.children[char]
        path += char

        if node.is_end_word:
            result.add(path)

        # Mark as visited
        board[i][j] = "#"

        # Explore neighbors
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(i + di, j + dj, node, path)

        # Backtrack
        board[i][j] = char

    for i in range(m):
        for j in range(n):
            dfs(i, j, trie.root, "")

    return list(result)
