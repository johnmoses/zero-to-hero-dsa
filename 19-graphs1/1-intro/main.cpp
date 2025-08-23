// Graph Introduction - C++ Example

#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    std::unordered_map<char, std::vector<char>> graph;
    graph['A'] = {'B', 'C'};
    graph['B'] = {'A', 'D'};
    graph['C'] = {'A', 'D'};
    graph['D'] = {'B', 'C'};

    std::cout << "Neighbors of node A: ";
    for (char neighbor : graph['A'])
        std::cout << neighbor << " ";
    std::cout << std::endl;
    return 0;
}
