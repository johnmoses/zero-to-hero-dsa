// Common Two Pointers Problems - Java Example

public class CommonTwoPointersProblems {

    public static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int width = right - left;
            int currArea = Math.min(height[left], height[right]) * width;
            maxArea = Math.max(maxArea, currArea);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] heights = {1,8,6,2,5,4,8,3,7};
        System.out.println("Max water container area: " + maxArea(heights));
    }
}
