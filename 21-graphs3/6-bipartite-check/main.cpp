// Bipartite Graph Check using BFS - C++ Example

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool isBipartite(const vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, -1);

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            queue<int> q;
            q.push(i);
            color[i] = 0;

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (int v : graph[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main() {
    vector<vector<int>> graph1 = {
        {1, 3},
        {0, 2},
        {1, 3},
        {0, 2}
    };

    vector<vector<int>> graph2 = {
        {1, 2},
        {0, 2},
        {0, 1}
    };

    cout << "Graph1 is bipartite: " << boolalpha << isBipartite(graph1) << endl;
    cout << "Graph2 is bipartite: " << boolalpha << isBipartite(graph2) << endl;

    return 0;
}
