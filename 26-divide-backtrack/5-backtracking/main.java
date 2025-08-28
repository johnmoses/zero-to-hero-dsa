// Backtracking - Java example (N-Queens)

import java.util.HashSet;

class Main {
    static int solutions = 0;

    public static boolean isNotUnderAttack(int row, int col, HashSet<Integer> cols,
                                           HashSet<Integer> hills, HashSet<Integer> dales) {
        return !cols.contains(col) && !hills.contains(row - col) && !dales.contains(row + col);
    }

    public static void placeQueen(int row, int col, HashSet<Integer> queensCols,
                                  HashSet<Integer> cols, HashSet<Integer> hills, HashSet<Integer> dales) {
        queensCols.add(col);
        cols.add(col);
        hills.add(row - col);
        dales.add(row + col);
    }

    public static void removeQueen(int row, int col, HashSet<Integer> queensCols,
                                   HashSet<Integer> cols, HashSet<Integer> hills, HashSet<Integer> dales) {
        queensCols.remove(col);
        cols.remove(col);
        hills.remove(row - col);
        dales.remove(row + col);
    }

    public static void backtrack(int n, int row, HashSet<Integer> queensCols,
                                 HashSet<Integer> cols, HashSet<Integer> hills, HashSet<Integer> dales) {
        if (row == n) {
            solutions++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isNotUnderAttack(row, col, cols, hills, dales)) {
                placeQueen(row, col, queensCols, cols, hills, dales);
                backtrack(n, row + 1, queensCols, cols, hills, dales);
                removeQueen(row, col, queensCols, cols, hills, dales);
            }
        }
    }

    public static void main(String[] args) {
        int n = 4;
        HashSet<Integer> queensCols = new HashSet<>();
        HashSet<Integer> cols = new HashSet<>();
        HashSet<Integer> hills = new HashSet<>();
        HashSet<Integer> dales = new HashSet<>();
        backtrack(n, 0, queensCols, cols, hills, dales);
        System.out.println("Number of solutions for " + n + "-Queens: " + solutions);
    }
}
