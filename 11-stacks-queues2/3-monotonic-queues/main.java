// Monotonic Queue - Java Example

import java.util.Deque;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;

public class MonotonicQueue {

    public static List<Integer> maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) {
                dq.pollLast();
            }
            dq.offerLast(i);

            if (dq.peekFirst() == i - k) {
                dq.pollFirst();
            }

            if (i >= k - 1) {
                result.add(nums[dq.peekFirst()]);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1,3,-1,-3,5,3,6,7};
        int k = 3;
        List<Integer> maxVals = maxSlidingWindow(nums, k);
        System.out.print("Sliding window maximum: ");
        for (int val : maxVals) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}
