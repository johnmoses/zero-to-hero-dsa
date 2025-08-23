// Bellman-Ford Algorithm - C++ Example

#include <iostream>
#include <vector>
#include <limits>

using namespace std;

void bellmanFord(int V, vector<vector<int>>& edges, int src) {
    vector<int> dist(V, numeric_limits<int>::max());
    dist[src] = 0;

    for (int i = 0; i < V -1; i++) {
        for (auto& edge : edges) {
            int u = edge[0], v = edge, w = edge;
            if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    // Check for negative weight cycle
    for (auto& edge : edges) {
        int u = edge[0], v = edge, w = edge;
        if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v]) {
            cout << "Graph contains negative weight cycle" << endl;
            return;
        }
    }

    for (int i = 0; i < V; i++) {
        cout << "Distance from 0 to " << i << " is " << dist[i] << endl;
    }
}

int main() {
    int V = 5;
    vector<vector<int>> edges = {
        {0,1,-1}, {0,2,4}, {1,2,3}, {1,3,2}, {1,4,2}, {3,2,5}, {3,1,1}, {4,3,-3}
    };

    bellmanFord(V, edges, 0);

    return 0;
}
