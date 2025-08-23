// Monotonic Stack - Java example (Next Greater Element)

import java.util.*;

public class Main {
    public static int[] nextGreaterElements(int[] nums) {
        int[] result = new int[nums.length];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                result[stack.pop()] = nums[i];
            }
            stack.push(i);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2, 1, 2, 4, 3};
        int[] res = nextGreaterElements(nums);
        System.out.println(Arrays.toString(res));  // Output: [4, 2, 4, -1, -1]
    }
}
