// Variable Size Sliding Window - Java Example

class VariableSizeSlidingWindow {

    public static int minSubarrayLen(int target, int[] arr) {
        int start = 0, currSum = 0, minLen = Integer.MAX_VALUE;

        for (int end = 0; end < arr.length; end++) {
            currSum += arr[end];
            while (currSum >= target) {
                minLen = Math.min(minLen, end - start + 1);
                currSum -= arr[start++];
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    public static void main(String[] args) {
        int[] arr = {2,3,1,2,4,3};
        int target = 7;
        System.out.println("Minimum subarray length with sum >= " + target + ": " + minSubarrayLen(target, arr));
    }
}
