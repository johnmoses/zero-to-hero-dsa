// Matrix Traversal and Search - C++ Example

#include <iostream>
#include <vector>

std::pair<int,int> searchInMatrix(const std::vector<std::vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int r = 0, c = cols - 1;

    while (r < rows && c >= 0) {
        if (matrix[r][c] == target)
            return {r, c};
        else if (matrix[r][c] > target)
            c--;
        else
            r++;
    }
    return {-1, -1};
}

int main() {
    std::vector<std::vector<int>> matrix{
        {1,4,7,11}, {2,5,8,12}, {3,6,9,16}, {10,13,14,17}
    };

    auto pos = searchInMatrix(matrix, 5);
    std::cout << "Target 5 at: (" << pos.first << ", " << pos.second << ")" << std::endl;
    return 0;
}
