// Cumulative Sums - Java Example

public class CumulativeSums {

    public static int[] cumulativeCountPositive(int[] arr) {
        int[] cumCount = new int[arr.length];
        cumCount[0] = arr > 0 ? 1 : 0;
        for (int i = 1; i < arr.length; i++) {
            cumCount[i] = cumCount[i - 1] + (arr[i] > 0 ? 1 : 0);
        }
        return cumCount;
    }

    public static void main(String[] args) {
        int[] arr = {-1, 4, 2, -3, 5};
        int[] countPos = cumulativeCountPositive(arr);

        System.out.print("Cumulative count of positives: ");
        for (int val : countPos) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}
