/**
 * Template II

Example 1:
    
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
 */

public class main {
    int binarySearch(int[] nums, int target){
    if(nums == null || nums.length == 0)
        return -1;

    int left = 0, right = nums.length - 1;
    while(left < right){
        // Prevent (left + right) overflow
        int mid = left + (right - left) / 2;
        if(nums[mid] == target){ return mid; }
        else if(nums[mid] < target) { left = mid + 1; }
        else { right = mid; }
    }

    // Post-processing:
    // End Condition: left == right
    if(nums[left] == target) return left;
    return -1;
    }
    public static void main(String[] args) {
        int[] nums = {-1,0,3,5,9,12};
        int target = 9;
        main m = new main();
        System.out.println(m.binarySearch(nums, target));
    }
}