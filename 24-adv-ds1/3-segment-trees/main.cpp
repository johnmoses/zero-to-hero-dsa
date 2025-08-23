// Segment Trees - C++ example (Range Sum Query)

#include <iostream>
#include <vector>

class SegmentTree {
    std::vector<int> tree;
    int n;

    void build(const std::vector<int>& data, int node, int start, int end) {
        if (start == end) {
            tree[node] = data[start];
        } else {
            int mid = (start + end) / 2;
            build(data, 2*node+1, start, mid);
            build(data, 2*node+2, mid+1, end);
            tree[node] = tree[2*node+1] + tree[2*node+2];
        }
    }

    void update(int idx, int val, int node, int start, int end) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid)
                update(idx, val, 2*node+1, start, mid);
            else
                update(idx, val, 2*node+2, mid+1, end);
            tree[node] = tree[2*node+1] + tree[2*node+2];
        }
    }

    int query(int l, int r, int node, int start, int end) {
        if (r < start || l > end) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return query(l, r, 2*node+1, start, mid) + query(l, r, 2*node+2, mid+1, end);
    }

public:
    SegmentTree(const std::vector<int>& data) {
        n = data.size();
        tree.resize(4*n);
        build(data, 0, 0, n-1);
    }

    void update(int idx, int val) {
        update(idx, val, 0, 0, n-1);
    }

    int query(int l, int r) {
        return query(l, r, 0, 0, n-1);
    }
};

int main() {
    std::vector<int> data = {1, 3, 5, 7, 9, 11};
    SegmentTree segTree(data);
    std::cout << segTree.query(1, 3) << std::endl;  // Output: 15
    segTree.update(1, 10);
    std::cout << segTree.query(1, 3) << std::endl;  // Output: 22
    return 0;
}
