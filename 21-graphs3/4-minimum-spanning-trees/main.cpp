// Prim's Algorithm for MST - C++ Example

#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

vector<pair<int,int>> primMST(const vector<vector<pair<int,int>>>& graph) {
    int V = graph.size();
    vector<bool> inMST(V, false);
    priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
    vector<pair<int,int>> mstEdges;
    int totalWeight = 0;

    pq.push({0, 0}); // weight, vertex
    vector<int> parent(V, -1);

    while (!pq.empty()) {
        int weight = pq.top().first;
        int vertex = pq.top().second;
        pq.pop();

        if (inMST[vertex]) continue;

        inMST[vertex] = true;
        totalWeight += weight;

        if (parent[vertex] != -1)
            mstEdges.push_back({parent[vertex], vertex});

        for (auto& [adj, w] : graph[vertex]) {
            if (!inMST[adj]) {
                pq.push({w, adj});
                parent[adj] = vertex;
            }
        }
    }

    cout << "Total weight of MST: " << totalWeight << endl;
    return mstEdges;
}

int main() {
    vector<vector<pair<int,int>>> graph = {
        {{1,2}, {3,6}},   // 0
        {{0,2}, {2,3}, {3,8}, {4,5}}, // 1
        {{1,3}, {4,7}},  // 2
        {{0,6}, {1,8}},  // 3
        {{1,5}, {2,7}}   // 4
    };

    auto mstEdges = primMST(graph);
    cout << "Edges in MST:\n";
    for (auto& edge : mstEdges) {
        cout << edge.first << " - " << edge.second << endl;
    }

    return 0;
}
