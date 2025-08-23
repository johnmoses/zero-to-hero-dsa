// Matrix Basics - Java Example

public class MatrixBasics {

    public static int[][] identityMatrix(int n) {
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            matrix[i][i] = 1;
        }
        return matrix;
    }

    public static void main(String[] args) {
        int[][] mat = identityMatrix(3);
        for (int[] row : mat) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
