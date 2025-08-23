# Segment Trees - Python example (Range Sum Query)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, 2 * node + 1, start, mid)
            else:
                self.update(idx, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right, node, start, end):
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        lsum = self.query(left, right, 2 * node + 1, start, mid)
        rsum = self.query(left, right, 2 * node + 2, mid + 1, end)
        return lsum + rsum

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)
    print(seg_tree.query(1, 3, 0, 0, seg_tree.n - 1))  # Output: 15
    seg_tree.update(1, 10, 0, 0, seg_tree.n - 1)
    print(seg_tree.query(1, 3, 0, 0, seg_tree.n - 1))  # Output: 22
