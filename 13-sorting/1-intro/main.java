// Sorting Introduction - Java Example

import java.util.Arrays;

public class SortingIntro {
    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 4, 2};
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);

        System.out.print("Original array: ");
        for (int x : arr) System.out.print(x + " ");
        System.out.print("\nSorted array: ");
        for (int x : sortedArr) System.out.print(x + " ");
        System.out.println();
    }
}
