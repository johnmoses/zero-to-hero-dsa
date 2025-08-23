// Matrix Operations - Java Example

public class MatrixOperations {

    public static int[][] addMatrices(int[][] A, int[][] B) {
        int n = A.length, m = A[0].length;
        int[][] result = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                result[i][j] = A[i][j] + B[i][j];
        return result;
    }

    public static int[][] transposeMatrix(int[][] A) {
        int n = A.length, m = A[0].length;
        int[][] result = new int[m][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                result[j][i] = A[i][j];
        return result;
    }

    public static void printMatrix(int[][] M) {
        for (int[] row : M) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] A = {{1,2}, {3,4}};
        int[][] B = {{5,6}, {7,8}};

        System.out.println("Added matrix:");
        printMatrix(addMatrices(A, B));

        System.out.println("Transposed matrix:");
        printMatrix(transposeMatrix(A));
    }
}
