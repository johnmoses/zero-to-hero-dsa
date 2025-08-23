// Array Types - Java Example

public class ArrayTypes {

    public static void main(String[] args) {
        // 1D array
        int[] arr1d = {1, 2, 3};

        // 2D array
        int[][] arr2d = {{1, 2}, {3, 4}};

        System.out.print("1D array: ");
        for (int num : arr1d) {
            System.out.print(num + " ");
        }
        System.out.println();

        System.out.println("2D array:");
        for (int[] row : arr2d) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
