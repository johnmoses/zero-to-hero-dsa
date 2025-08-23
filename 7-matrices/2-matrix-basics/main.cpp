// Matrix Basics - C++ Example

#include <iostream>
#include <vector>

std::vector<std::vector<int>> identityMatrix(int n) {
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        matrix[i][i] = 1;
    }
    return matrix;
}

int main() {
    auto mat = identityMatrix(3);
    for (const auto& row : mat) {
        for (int val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
