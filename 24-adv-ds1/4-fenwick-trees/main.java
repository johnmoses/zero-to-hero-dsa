// Fenwick Trees - Java example

class Main {
    static class FenwickTree {
        int[] tree;
        int size;

        FenwickTree(int n) {
            size = n;
            tree = new int[n + 1];
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
    }

    public static void main(String[] args) {
        int n = 6;
        FenwickTree ft = new FenwickTree(n);
        int[] data = {1, 3, 5, 7, 9, 11};
        for (int i = 1; i <= n; i++) {
            ft.update(i, data[i - 1]);
        }

        System.out.println(ft.query(3));  // Output: 9
        ft.update(3, 2);
        System.out.println(ft.query(3));  // Output: 11
    }
}
