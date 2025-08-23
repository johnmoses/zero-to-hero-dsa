// Matrix Traversal and Search - Java Example

public class MatrixTraversalSearch {

    public static int[] searchInMatrix(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;
        int r = 0, c = cols - 1;
        while (r < rows && c >= 0) {
            if (matrix[r][c] == target) {
                return new int[]{r, c};
            } else if (matrix[r][c] > target) {
                c--;
            } else {
                r++;
            }
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1,4,7,11},
            {2,5,8,12},
            {3,6,9,16},
            {10,13,14,17}
        };

        int[] pos = searchInMatrix(matrix, 5);
        System.out.println("Target 5 at: (" + pos[0] + ", " + pos + ")");
    }
}
