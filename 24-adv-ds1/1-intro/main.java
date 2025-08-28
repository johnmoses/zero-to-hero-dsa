// Advanced Data Structures 1 - Intro Java example

class Main {
    static class UnionFind {
        int[] parent, rank;
        public UnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
        }
    }

    public static void main(String[] args) {
        UnionFind uf = new UnionFind(5);
        System.out.println("Union-Find initialized for 5 elements.");
    }
}
