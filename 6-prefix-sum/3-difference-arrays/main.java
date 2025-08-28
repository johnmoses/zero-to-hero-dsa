// Difference Arrays - Java Example

class DifferenceArrays {

    public static void updateRange(int[] diff, int l, int r, int val) {
        diff[l] += val;
        if (r + 1 < diff.length) {
            diff[r + 1] -= val;
        }
    }

    public static int[] reconstructArray(int[] diff) {
        int[] res = new int[diff.length - 1];
        int curr = 0;
        for (int i = 0; i < res.length; i++) {
            curr += diff[i];
            res[i] = curr;
        }
        return res;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] diff = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) {
            diff[i] += arr[i];
            diff[i + 1] -= arr[i];
        }

        updateRange(diff, 1, 3, 5);
        int[] result = reconstructArray(diff);

        System.out.print("Array after range update: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}
