// Depth-First Search (DFS) - C++ Example

#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>

void dfs(const std::unordered_map<char, std::vector<char>>& graph, char node, std::unordered_set<char>& visited) {
    visited.insert(node);
    std::cout << node << " ";
    for (char neighbor : graph.at(node)) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited);
        }
    }
}

int main() {
    std::unordered_map<char, std::vector<char>> graph = {
        {'A', {'B', 'C'}},
        {'B', {'D'}},
        {'C', {'D'}},
        {'D', {}}
    };

    std::unordered_set<char> visited;
    std::cout << "DFS traversal starting from A: ";
    dfs(graph, 'A', visited);
    std::cout << std::endl;

    return 0;
}
