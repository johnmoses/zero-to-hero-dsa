// Fenwick Trees - C++ example

#include <iostream>
#include <vector>

class FenwickTree {
    std::vector<int> tree;
    int size;

public:
    FenwickTree(int n) : size(n) {
        tree.assign(n + 1, 0);
    }

    void update(int idx, int delta) {
        while (idx <= size) {
            tree[idx] += delta;
            idx += idx & (-idx);
        }
    }

    int query(int idx) {
        int result = 0;
        while (idx > 0) {
            result += tree[idx];
            idx -= idx & (-idx);
        }
        return result;
    }
};

int main() {
    int n = 6;
    FenwickTree ft(n);
    int data[] = {1, 3, 5, 7, 9, 11};
    for(int i = 1; i <= n; i++)
        ft.update(i, data[i-1]);

    std::cout << ft.query(3) << std::endl;  // Output: 9
    ft.update(3, 2);
    std::cout << ft.query(3) << std::endl;  // Output: 11
    return 0;
}
