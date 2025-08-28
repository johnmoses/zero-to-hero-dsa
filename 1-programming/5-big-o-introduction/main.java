// main.java
// Examples demonstrating Big-O time complexity in Java

class BigOExamples {

    public static int constantTimeExample(int[] arr) {
        // O(1) - Accessing first element
        return arr[0];
    }

    public static void linearTimeExample(int[] arr) {
        // O(n) - Loop through all elements
        for(int item : arr) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void quadraticTimeExample(int[] arr) {
        // O(n^2) - Nested loops
        for(int i : arr) {
            for(int j : arr) {
                System.out.print("(" + i + "," + j + ") ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[] sample = {1, 2, 3, 4};

        System.out.println("Constant time example:");
        System.out.println(constantTimeExample(sample));

        System.out.println("\nLinear time example:");
        linearTimeExample(sample);

        System.out.println("\nQuadratic time example:");
        quadraticTimeExample(sample);
    }
}
