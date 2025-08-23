// Topological Sorting - C++ Example (DFS based)

#include <iostream>
#include <vector>
#include <stack>

void topologicalSortUtil(int v, std::vector<std::vector<int>>& adj, std::vector<bool>& visited, std::stack<int>& st) {
    visited[v] = true;
    for (int neighbor : adj[v]) {
        if (!visited[neighbor])
            topologicalSortUtil(neighbor, adj, visited, st);
    }
    st.push(v);
}

std::vector<std::vector<int>> constructAdj(int V, std::vector<std::pair<int,int>>& edges) {
    std::vector<std::vector<int>> adj(V);
    for (auto& edge : edges) {
        adj[edge.first].push_back(edge.second);
    }
    return adj;
}

std::vector<int> topologicalSort(int V, std::vector<std::pair<int,int>>& edges) {
    auto adj = constructAdj(V, edges);
    std::vector<bool> visited(V, false);
    std::stack<int> st;

    for (int i = 0; i < V; i++) {
        if (!visited[i])
            topologicalSortUtil(i, adj, visited, st);
    }

    std::vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
    }
    return result;
}

int main() {
    int V = 6;
    std::vector<std::pair<int,int>> edges = {{2,3}, {3,1}, {4,0}, {4,1}, {5,0}, {5,2}};
    auto result = topologicalSort(V, edges);
    std::cout << "Topological sort order: ";
    for (int v : result) std::cout << v << " ";
    std::cout << std::endl;
    return 0;
}
