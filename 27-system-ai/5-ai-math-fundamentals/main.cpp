// AI Math Fundamentals - C++ example (Matrix multiplication)

#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> matMul(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int n = A.size(), m = B[0].size(), p = B.size();
    vector<vector<int>> C(n, vector<int>(m, 0));

    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            for(int k=0; k<p; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return C;
}

int main() {
    vector<vector<int>> A = {{1,2},{3,4}};
    vector<vector<int>> B = {{5,6},{7,8}};
    vector<vector<int>> C = matMul(A, B);

    cout << "Matrix multiplication result:" << endl;
    for(auto& row : C) {
        for(auto val : row) cout << val << " ";
        cout << endl;
    }
    return 0;
}
