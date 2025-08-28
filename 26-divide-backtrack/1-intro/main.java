// Divide and Conquer & Backtracking - Java example

import java.util.*;

class Main {
    // Merge function for merge sort
    public static List<Integer> merge(List<Integer> left, List<Integer> right) {
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        while (i < left.size() && j < right.size()) {
            if (left.get(i) < right.get(j)) result.add(left.get(i++));
            else result.add(right.get(j++));
        }
        while (i < left.size()) result.add(left.get(i++));
        while (j < right.size()) result.add(right.get(j++));
        return result;
    }

    // Merge sort using divide and conquer
    public static List<Integer> mergeSort(List<Integer> arr) {
        if (arr.size() <= 1) return arr;
        int mid = arr.size() / 2;
        return merge(mergeSort(arr.subList(0, mid)), mergeSort(arr.subList(mid, arr.size())));
    }

    // Backtracking subset sum
    public static boolean subsetSum(List<Integer> nums, int target, int index) {
        if (target == 0) return true;
        if (target < 0 || index == nums.size()) return false;

        // Include nums.get(index)
        if (subsetSum(nums, target - nums.get(index), index + 1)) return true;

        // Exclude nums.get(index)
        return subsetSum(nums, target, index + 1);
    }

    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(3, 6, 1, 7, 2, 5);
        List<Integer> sortedArr = mergeSort(arr);
        System.out.println("Sorted array: " + sortedArr);

        List<Integer> nums = Arrays.asList(3, 34, 4, 12, 5, 2);
        int target = 9;
        System.out.println("Subset sum exists: " + subsetSum(nums, target, 0));
    }
}
