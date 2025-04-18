/**
 * Given a set of numbers, write a divide and conquer algorithm to sort the numbers.

Example 1:
    Input: [3, 7, 6, -10, 15, 23.5, 55, -13]
    Output: [-13, -10, 3, 6, 7, 15, 23.5, 55]
 */
public class main {
    public static double[] sort(double[] arr) {
        if (arr == null || arr.length <= 1) return arr;
        return mergeSort(arr, 0, arr.length - 1);
    }


    private static double[] mergeSort(double[] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
        return arr;
    }

    private static void merge(double[] arr, int start, int mid, int end) {

        double[] temp = new double[end - start + 1];
        int i = start, j = mid + 1, k = 0;
        
        while (i <= mid && j <= end) {
            if (arr[i] <= arr[j]) temp[k++] = arr[i++];
            else temp[k++] = arr[j++];
        }
        
        while (i <= mid) temp[k++] = arr[i++];
        while (j <= end) temp[k++] = arr[j++];

        
        for (i = 0; i < temp.length; i++) {
            arr[start + i] = temp[i];
        }
    }

    public static void main(String[] args) {
        double[] arr = {3, 7, 6, -10, 15, 23.5, 55, -13};
        double[] sortedArr = sort(arr);
        for (double num : sortedArr) {
            System.out.print(num + " ");
        }
    }
}