// Backtracking - C++ example (N-Queens)

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool isNotUnderAttack(int row, int col, unordered_set<int>& cols,
                      unordered_set<int>& hills, unordered_set<int>& dales) {
    return cols.find(col) == cols.end() &&
           hills.find(row - col) == hills.end() &&
           dales.find(row + col) == dales.end();
}

void placeQueen(int row, int col, unordered_set<int>& queensCols,
                unordered_set<int>& cols, unordered_set<int>& hills,
                unordered_set<int>& dales) {
    queensCols.insert(col);
    cols.insert(col);
    hills.insert(row - col);
    dales.insert(row + col);
}

void removeQueen(int row, int col, unordered_set<int>& queensCols,
                 unordered_set<int>& cols, unordered_set<int>& hills,
                 unordered_set<int>& dales) {
    queensCols.erase(col);
    cols.erase(col);
    hills.erase(row - col);
    dales.erase(row + col);
}

void backtrack(int n, int row, unordered_set<int>& queensCols,
               unordered_set<int>& cols, unordered_set<int>& hills,
               unordered_set<int>& dales, int& solutions) {
    if (row == n) {
        solutions++;
        return;
    }
    for (int col = 0; col < n; ++col) {
        if (isNotUnderAttack(row, col, cols, hills, dales)) {
            placeQueen(row, col, queensCols, cols, hills, dales);
            backtrack(n, row + 1, queensCols, cols, hills, dales, solutions);
            removeQueen(row, col, queensCols, cols, hills, dales);
        }
    }
}

int main() {
    int n = 4;
    unordered_set<int> queensCols, cols, hills, dales;
    int solutions = 0;
    backtrack(n, 0, queensCols, cols, hills, dales, solutions);
    cout << "Number of solutions for " << n << "-Queens: " << solutions << endl;
    return 0;
}
