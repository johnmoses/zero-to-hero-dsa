/*
 Graph Representation

 Given the nodes ['A', 'B', 'C', 'D', 'E'] and 
 edges edges = [
    [0, 1, 1, 1, 0],  # Edges for A
    [1, 0, 1, 0, 0],  # Edges for B
    [1, 1, 0, 0, 0],  # Edges for C
    [1, 0, 0, 0, 0],  # Edges for D
    [0, 1, 0, 0, 1]   # Edges for E
], Write a basic adjacency matrix graph representation in C++.
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<string> nodes = {"A", "B", "C", "D", "E"};
    vector<vector<int>> edges = {
        {0, 1, 1, 1, 0},
        {1, 0, 1, 0, 0},
        {1, 1, 0, 0, 0},
        {1, 0, 0, 0, 0},
        {0, 0, 0, 0, 0}
    };

    cout << "Adjacency Matrix:" << endl;
    cout << "  ";
    for (const string& node : nodes) {
        cout << node << " ";
    }
    cout << endl;

    for (size_t i = 0; i < edges.size(); ++i) {
        cout << nodes[i] << " ";
        for (int edge : edges[i]) {
            cout << edge << " ";
        }
        cout << endl;
    }

    return 0;
}
