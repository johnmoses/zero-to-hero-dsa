/**
 * Bubble Sort

Example 1:
    Input: [64, 34, 25, 12, 22, 11, 90, 5]
    Output: [11, 12, 22, 25, 34, 5, 64, 90]
 */
class main {
    public int[] sortArray1(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
        return nums;
    }

    public int[] sortArray2(int[] nums) {
        // Mutates arr so that it is sorted via swapping adjacent elements until
        // the arr is sorted.
        boolean hasSwapped = true;
        while (hasSwapped) {
            hasSwapped = false;
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] > nums[i + 1]) {
                    // Swap adjacent elements
                    int temp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = temp;
                    hasSwapped = true;
                }
            }
        }
        return nums;
    }

    public static void main(String[] args) {
        int[] nums = {64, 34, 25, 12, 22, 11, 90, 5};
        main m = new main();

        int[] sorted = m.sortArray1(nums);
        for (int i = 0; i < sorted.length; i++) {
            System.out.print(sorted[i] + " ");
        }

        System.out.println();
        
        int[] sorted2 = m.sortArray2(nums);
        for (int i = 0; i < sorted2.length; i++) {
            System.out.print(sorted2[i] + " ");
        }
    }
}
