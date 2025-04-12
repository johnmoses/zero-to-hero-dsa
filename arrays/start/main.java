/* 
Arrays

Write code to show the basic functionality or behavior of an array.
This includes selecting, slicing, updating, adding, removing, sorting, searching and so on.
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class main {
    public static void main(String[] args) {
        int[] arr = createArray();
        System.out.println("Original Array: " + Arrays.toString(arr));
        int[] slice = sliceArray(arr, 1, 4);
        System.out.println("Sliced Array: " + Arrays.toString(slice));
        updateElement(arr, 2, 10);
        System.out.println("Updated Array: " + Arrays.toString(arr));
        int[] newArr = addElement(arr, 15);
        System.out.println("Added Element Array: " + Arrays.toString(newArr));
        int[] remArr = removeElement(arr, 3);
        System.out.println("Removed Element Array: " + Arrays.toString(remArr));
        sortArray(arr);
        System.out.println("Sorted Array: " + Arrays.toString(arr));
        int index = searchElement(arr, 8);
        System.out.println("Element 8 found at index: " + index);
        reverseArray(arr);
        System.out.println("Reversed Array: " + Arrays.toString(arr));
    }

    // Initialize and select elements
    public static int[] createArray() {
        int[] numbers = {1, 5, 3, 8, 2, 9, 4};
        return numbers;
    }


    // Slice array from start to end index
    public static int[] sliceArray(int[] arr, int start, int end) {
        int[] slice = Arrays.copyOfRange(arr, start, end);
        return slice;
    }


    // Update element at specific index
    public static void updateElement(int[] arr, int index, int value) {
        arr[index] = value;
    }


    // Add element to end using ArrayList
    public static int[] addElement(int[] arr, int element) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int num : arr) list.add(num);
        list.add(element);
        return list.stream().mapToInt(i -> i).toArray();
    }


    // Remove element at index
    public static int[] removeElement(int[] arr, int index) {
        int[] newArr = new int[arr.length - 1];
        System.arraycopy(arr, 0, newArr, 0, index);
        System.arraycopy(arr, index + 1, newArr, index, arr.length - index - 1);
        return newArr;
    }


    // Sort array in ascending order
    public static void sortArray(int[] arr) {
        Arrays.sort(arr);
    }


    // Search element in array
    public static int searchElement(int[] arr, int element) {
        return Arrays.binarySearch(arr, element);
    }


    // Reverse array
    public static void reverseArray(int[] arr) {
        for(int i = 0; i < arr.length/2; i++) {
            int temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
    }
}
