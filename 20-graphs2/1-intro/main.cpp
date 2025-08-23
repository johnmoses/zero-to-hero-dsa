// Advanced Graph Algorithms Introduction - C++ Example

#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
    std::unordered_map<int, std::vector<int>> graph;
    graph[0] = {1, 2};
    graph[11] = {0};
    graph[10] = {0, 3};
    graph[12] = {2};

    std::cout << "Graph vertices: ";
    for (auto& pair : graph) std::cout << pair.first << " ";
    std::cout << "\nGraph edges from 0: ";
    for (int v : graph) std::cout << v << " ";
    std::cout << std::endl;

    return 0;
}
