// Merge Sort - Java Example

import java.util.Arrays;

class MergeSort {

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) return arr;

        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    private static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i=0, j=0, k=0;

        while(i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }
        while(i < left.length) result[k++] = left[i++];
        while(j < right.length) result[k++] = right[j++];

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {38,27,43,3,9,82,10};
        int[] sortedArr = mergeSort(arr);

        System.out.print("Sorted array: ");
        for (int x : sortedArr) System.out.print(x + " ");
        System.out.println();
    }
}
