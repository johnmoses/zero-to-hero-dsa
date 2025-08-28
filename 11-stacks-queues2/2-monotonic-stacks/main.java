// Monotonic Stack - Java Example

import java.util.Stack;

class MonotonicStack {

    public static int[] nextGreaterElements(int[] arr) {
        int[] result = new int[arr.length];
        java.util.Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < arr.length; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
                int idx = stack.pop();
                result[idx] = arr[i];
            }
            stack.push(i);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {2,1,2,4,3};
        int[] result = nextGreaterElements(arr);
        System.out.print("Next greater elements: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}
