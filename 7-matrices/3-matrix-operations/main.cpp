// Matrix Operations - C++ Example

#include <iostream>
#include <vector>

using Matrix = std::vector<std::vector<int>>;

Matrix addMatrices(const Matrix& A, const Matrix& B) {
    int n = A.size(), m = A[0].size();
    Matrix result(n, std::vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            result[i][j] = A[i][j] + B[i][j];
    return result;
}

Matrix transposeMatrix(const Matrix& A) {
    int n = A.size(), m = A[0].size();
    Matrix result(m, std::vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            result[j][i] = A[i][j];
    return result;
}

void printMatrix(const Matrix& M) {
    for (const auto& row : M) {
        for (int val : row)
            std::cout << val << " ";
        std::cout << std::endl;
    }
}

int main() {
    Matrix A = {{1,2},{3,4}};
    Matrix B = {{5,6},{7,8}};

    std::cout << "Added matrix:" << std::endl;
    Matrix C = addMatrices(A, B);
    printMatrix(C);

    std::cout << "Transposed matrix:" << std::endl;
    Matrix T = transposeMatrix(A);
    printMatrix(T);

    return 0;
}
