// Matrix Problems - C++ Example

#include <iostream>
#include <vector>

void rotateMatrix90(std::vector<std::vector<int>>& matrix) {
    int n = matrix.size();
    for (int layer = 0; layer < n / 2; layer++) {
        int first = layer;
        int last = n - layer - 1;
        for (int i = first; i < last; i++) {
            int offset = i - first;
            int top = matrix[first][i];
            // left -> top
            matrix[first][i] = matrix[last - offset][first];
            // bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset];
            // right -> bottom
            matrix[last][last - offset] = matrix[i][last];
            // top -> right
            matrix[i][last] = top;
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    rotateMatrix90(matrix);
    for (auto& row : matrix) {
        for (auto val : row) std::cout << val << " ";
        std::cout << std::endl;
    }
    return 0;
}
