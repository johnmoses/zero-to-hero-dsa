// Problem Applications - Java Example

import java.util.Stack;

public class ProblemApplications {

    public static int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int[] extendedHeights = new int[heights.length + 1];
        System.arraycopy(heights, 0, extendedHeights, 0, heights.length);

        for (int i = 0; i < extendedHeights.length; i++) {
            while (!stack.isEmpty() && extendedHeights[stack.peek()] > extendedHeights[i]) {
                int height = extendedHeights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] heights = {2,1,5,6,2,3};
        System.out.println("Largest rectangle area: " + largestRectangleArea(heights));
    }
}
