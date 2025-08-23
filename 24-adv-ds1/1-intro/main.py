# Advanced Data Structures 1 - Intro Python example
# Example: Basic Union-Find structure initialization

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

if __name__ == "__main__":
    uf = UnionFind(5)
    print("Union-Find initialized for 5 elements.")
