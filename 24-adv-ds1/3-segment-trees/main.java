// Segment Trees - Java example (Range Sum Query)

public class Main {
    static class SegmentTree {
        int[] tree;
        int n;

        public SegmentTree(int[] data) {
            n = data.length;
            tree = new int[4 * n];
            build(data, 0, 0, n - 1);
        }

        private void build(int[] data, int node, int start, int end) {
            if (start == end) {
                tree[node] = data[start];
            } else {
                int mid = (start + end) / 2;
                build(data, 2 * node + 1, start, mid);
                build(data, 2 * node + 2, mid + 1, end);
                tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
            }
        }

        public void update(int idx, int val) {
            update(idx, val, 0, 0, n - 1);
        }

        private void update(int idx, int val, int node, int start, int end) {
            if (start == end) {
                tree[node] = val;
            } else {
                int mid = (start + end) / 2;
                if (idx <= mid)
                    update(idx, val, 2 * node + 1, start, mid);
                else
                    update(idx, val, 2 * node + 2, mid + 1, end);
                tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
            }
        }

        public int query(int left, int right) {
            return query(left, right, 0, 0, n - 1);
        }

        private int query(int left, int right, int node, int start, int end) {
            if (right < start || left > end)
                return 0;
            if (left <= start && end <= right)
                return tree[node];
            int mid = (start + end) / 2;
            int leftSum = query(left, right, 2 * node + 1, start, mid);
            int rightSum = query(left, right, 2 * node + 2, mid + 1, end);
            return leftSum + rightSum;
        }
    }

    public static void main(String[] args) {
        int[] data = {1, 3, 5, 7, 9, 11};
        SegmentTree segTree = new SegmentTree(data);
        System.out.println(segTree.query(1, 3));  // Output: 15
        segTree.update(1, 10);
        System.out.println(segTree.query(1, 3));  // Output: 22
    }
}
