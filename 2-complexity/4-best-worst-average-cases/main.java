// Best, Worst, and Average Case - Java Example

public class BestWorstAverage {

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] data = {1, 2, 3, 4, 5};

        System.out.println("Best case (target=1): " + linearSearch(data, 1));
        System.out.println("Worst case (target=6): " + linearSearch(data, 6));
        System.out.println("Average case (target=3): " + linearSearch(data, 3));
    }
}
