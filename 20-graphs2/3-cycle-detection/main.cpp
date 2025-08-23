// Cycle Detection in Directed Graph - C++ Example

#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>

bool isCyclicUtil(const std::unordered_map<int, std::vector<int>>& graph, int v,
    std::unordered_set<int>& visited, std::unordered_set<int>& recStack) {

    visited.insert(v);
    recStack.insert(v);

    for (int neighbor : graph.at(v)) {
        if (visited.find(neighbor) == visited.end()) {
            if (isCyclicUtil(graph, neighbor, visited, recStack))
                return true;
        }
        else if (recStack.find(neighbor) != recStack.end())
            return true;
    }

    recStack.erase(v);
    return false;
}

bool isCyclic(const std::unordered_map<int, std::vector<int>>& graph) {
    std::unordered_set<int> visited;
    std::unordered_set<int> recStack;

    for (auto& pair : graph) {
        int node = pair.first;
        if (visited.find(node) == visited.end()) {
            if (isCyclicUtil(graph, node, visited, recStack)) 
                return true;
        }
    }
    return false;
}

int main() {
    std::unordered_map<int, std::vector<int>> graph = {
        {0, {1}},
        {1, {2}},
        {2, {0}}
    };

    std::cout << "Graph contains cycle: " << (isCyclic(graph) ? "true" : "false") << std::endl;
    return 0;
}
