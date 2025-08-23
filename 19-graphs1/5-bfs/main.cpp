// Breadth-First Search (BFS) - C++ Example

#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>

void bfs(const std::unordered_map<char, std::vector<char>>& graph, char start) {
    std::unordered_set<char> visited;
    std::queue<char> q;
    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        char node = q.front();
        q.pop();
        std::cout << node << " ";
        for (char neighbor : graph.at(node)) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
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

    std::cout << "BFS traversal starting from A: ";
    bfs(graph, 'A');
    std::cout << std::endl;

    return 0;
}
