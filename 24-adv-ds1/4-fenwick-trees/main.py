# Fenwick Trees - Python example

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result

if __name__ == "__main__":
    ft = FenwickTree(6)
    data = [1, 3, 5, 7, 9, 11]
    for i, val in enumerate(data, 1):
        ft.update(i, val)

    print(ft.query(3))  # Output: 9 (sum of first 3 elements)
    ft.update(3, 2)    # Increment 3rd element by 2
    print(ft.query(3))  # Output: 11
