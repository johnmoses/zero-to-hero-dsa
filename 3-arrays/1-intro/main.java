// Arrays - Java Example

public class ArraysIntro {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        System.out.println("Element at index 2: " + arr[2]); // Output: 3

        arr = 10;

        System.out.print("Modified array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
