// Union Find - C++ example

#include <iostream>
#include <vector>

class UnionFind {
public:
    std::vector<int> parent, rank;
    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 0);
        for(int i = 0; i < size; i++)
            parent[i] = i;
    }

    int find(int x) {
        if(parent[x] != x)
            parent[x] = find(parent[x]);  // Path compression
        return parent[x];
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if(rootX != rootY) {
            if(rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else if(rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int main() {
    UnionFind uf(5);
    uf.unionSet(0,1);
    uf.unionSet(1,2);
    std::cout << (uf.find(0) == uf.find(2)) << std::endl;  // Output: 1 (true)
    std::cout << (uf.find(3) == uf.find(2)) << std::endl;  // Output: 0 (false)
    return 0;
}
