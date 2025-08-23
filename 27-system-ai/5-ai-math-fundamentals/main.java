// AI Math Fundamentals - Java example (Matrix multiplication)

public class Main {
    public static int[][] matMul(int[][] A, int[][] B) {
        int n = A.length;
        int m = B[0].length;
        int p = B.length;
        int[][] C = new int[n][m];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                for(int k = 0; k < p; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return C;
    }

    public static void main(String[] args) {
        int[][] A = {{1, 2}, {3, 4}};
        int[][] B = {{5, 6}, {7, 8}};
        int[][] C = matMul(A, B);

        System.out.println("Matrix multiplication result:");
        for (int[] row : C) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
