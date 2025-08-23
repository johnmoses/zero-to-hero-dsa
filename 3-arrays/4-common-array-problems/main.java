// Common Array Problems - Java Example

import java.util.Arrays;

public class CommonArrayProblems {

    public static void main(String[] args) {
        int[] arr = {1, 3, 2, 8, 5};

        // Find maximum
        int maxVal = Arrays.stream(arr).max().getAsInt();
        System.out.println("Maximum value: " + maxVal);

        // Reverse array
        for (int i = 0; i < arr.length / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
        System.out.print("Reversed array: ");
        for (int val : arr) {
            System.out.print(val + " ");
        }
        System.out.println();

        // Sum of subarray [1, 4)
        int subSum = 0;
        for (int i = 1; i < 4; i++) {
            subSum += arr[i];
        }
        System.out.println("Subarray sum: " + subSum);
    }
}
