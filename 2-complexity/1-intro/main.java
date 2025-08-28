// Introduction to Complexity - Java Example

class ComplexityIntro {

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] data = {4, 7, 1, 3, 9};
        System.out.println("Index of 3: " + linearSearch(data, 3));
    }
}
