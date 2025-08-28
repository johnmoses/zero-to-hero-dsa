// Prefix Sum - Java Example

class PrefixSum {

    public static int[] prefixSum(int[] arr) {
        int[] prefix = new int[arr.length];
        prefix[0] = arr[0];
        for (int i = 1; i < arr.length; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }
        return prefix;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int[] prefix = prefixSum(arr);

        System.out.print("Prefix sum array: ");
        for (int val : prefix) {
            System.out.print(val + " ");
        }
        System.out.println();

        int result = prefix[3] - prefix[0];
        System.out.println("Sum from index 1 to 3: " + result);
    }
}
