// main.cpp
// Examples demonstrating Big-O time complexity in C++

#include <iostream>
#include <vector>

int constantTimeExample(const std::vector<int>& arr) {
    // O(1) - Accessing first element
    return arr[0];
}

void linearTimeExample(const std::vector<int>& arr) {
    // O(n) - Loop through all elements
    for(int item : arr) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}

void quadraticTimeExample(const std::vector<int>& arr) {
    // O(n^2) - Nested loops
    for(int i : arr) {
        for(int j : arr) {
            std::cout << "(" << i << "," << j << ") ";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<int> sample = {1, 2, 3, 4};

    std::cout << "Constant time example:" << std::endl;
    std::cout << constantTimeExample(sample) << std::endl;

    std::cout << "\nLinear time example:" << std::endl;
    linearTimeExample(sample);

    std::cout << "\nQuadratic time example:" << std::endl;
    quadraticTimeExample(sample);

    return 0;
}
