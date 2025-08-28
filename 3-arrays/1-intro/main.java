// Arrays - Java Example

class ArraysIntro {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        System.out.println("Element at index 2: " + arr[2]); // Output: 3

        // arr = 10; // This line would cause a compile-time error: Type mismatch: cannot convert from int to int[]

        System.out.print("Modified array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
