// Graph Types - C++ Example

#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    std::unordered_map<char, std::vector<char>> directed_graph;
    directed_graph['A'] = {'B'};
    directed_graph['B'] = {'C'};
    directed_graph['C'] = {};

    std::unordered_map<char, std::vector<std::pair<char, int>>> weighted_graph;
    weighted_graph['A'] = {{'B', 4}, {'C', 3}};
    weighted_graph['B'] = {{'A', 4}, {'C', 1}};
    weighted_graph['C'] = {{'A', 3}, {'B', 1}};

    std::cout << "Directed graph edges from A: ";
    for (auto c : directed_graph['A']) std::cout << c << " ";
    std::cout << std::endl;

    std::cout << "Weighted edges from A: ";
    for (auto p : weighted_graph['A']) {
        std::cout << "(" << p.first << ", " << p.second << ") ";
    }
    std::cout << std::endl;

    return 0;
}
