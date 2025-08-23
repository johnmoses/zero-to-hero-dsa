// Searching Introduction - Java Example

public class SearchingIntro {

    public static int linearSearch(int[] arr, int target) {
        for(int i=0; i < arr.length; i++) {
            if(arr[i] == target) return i;
        }
        return -1;
    }

    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length -1;
        while(low <= high) {
            int mid = low + (high - low)/2;
            if(arr[mid] == target) return mid;
            else if(arr[mid] < target) low = mid +1;
            else high = mid -1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2,4,6,8,10};
        System.out.println("Linear search index: " + linearSearch(arr, 8));
        System.out.println("Binary search index: " + binarySearch(arr, 8));
    }
}
