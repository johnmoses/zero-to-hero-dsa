// Dijkstra's Algorithm - C++ Example

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>

using namespace std;

unordered_map<char, vector<pair<char,int>>> buildGraph() {
    unordered_map<char, vector<pair<char,int>>> graph;
    graph['A'] = {{'B',1}, {'C',4}};
    graph['B'] = {{'C',2}, {'D',5}};
    graph['C'] = {{'D',1}};
    graph['D'] = {};
    return graph;
}

unordered_map<char,int> dijkstra(unordered_map<char, vector<pair<char,int>>>& graph, char start) {
    unordered_map<char,int> distances;
    for (auto& [node,_] : graph) distances[node] = numeric_limits<int>::max();
    distances[start] = 0;

    priority_queue<pair<int,char>, vector<pair<int,char>>, greater<>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [dist, node] = pq.top(); pq.pop();

        if (dist > distances[node]) continue;

        for (auto& [neighbor, weight] : graph[node]) {
            int newDist = dist + weight;
            if (newDist < distances[neighbor]) {
                distances[neighbor] = newDist;
                pq.push({newDist, neighbor});
            }
        }
    }
    return distances;
}

int main() {
    auto graph = buildGraph();
    auto distances = dijkstra(graph, 'A');
    cout << "Shortest distances from A:" << endl;
    for (auto& [node, dist] : distances) {
        cout << node << ": " << dist << endl;
    }
    return 0;
}

