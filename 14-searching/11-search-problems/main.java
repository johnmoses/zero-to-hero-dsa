// Search Problem Examples - Java Example

class SearchProblems {

    public static int countOnes(int[] arr) {
        int low = 0, high = arr.length - 1;
        int count = 0;
        while (low <= high) {
            int mid = low + (high - low)/2;
            if (arr[mid] == 1) {
                count = arr.length - mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] arr = {0,0,0,1,1,1,1};
        System.out.println("Count of ones: " + countOnes(arr));
    }
}
