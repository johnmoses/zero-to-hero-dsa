// Advanced Data Structures 1 - Intro C++ example

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
};

int main() {
    UnionFind uf(5);
    std::cout << "Union-Find initialized for 5 elements." << std::endl;
    return 0;
}
