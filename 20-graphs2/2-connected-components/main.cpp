// Connected Components - C++ Example (Undirected graph)

#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>

void dfs(const std::unordered_map<int, std::vector<int>>& graph, int node, std::unordered_set<int>& visited, std::vector<int>& comp) {
    visited.insert(node);
    comp.push_back(node);
    for (int neighbor : graph.at(node)) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited, comp);
        }
    }
}

std::vector<std::vector<int>> connectedComponents(const std::unordered_map<int, std::vector<int>>& graph) {
    std::unordered_set<int> visited;
    std::vector<std::vector<int>> components;
    for (auto& pair : graph) {
        int node = pair.first;
        if (visited.find(node) == visited.end()) {
            std::vector<int> comp;
            dfs(graph, node, visited, comp);
            components.push_back(comp);
        }
    }
    return components;
}

int main() {
    std::unordered_map<int, std::vector<int>> graph = {
        {0, {1}},
        {1, {0, 2}},
        {2, {1}},
        {3, {}}
    };

    auto comps = connectedComponents(graph);
    std::cout << "Connected Components:\n";
    for (auto& comp : comps) {
        for (int v : comp) std::cout << v << " ";
        std::cout << std::endl;
    }

    return 0;
}
