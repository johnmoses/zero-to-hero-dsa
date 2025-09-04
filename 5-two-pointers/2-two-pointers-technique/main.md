# The Two Pointers Technique

## Introduction
The two pointers technique involves using two indices to scan a data structure in a coordinated way, commonly for sorting or searching problems.

## Details
Pointers can start at the beginning and end and move towards each other, or both can move forward at different speeds.

Common use cases are finding pairs, removing duplicates, merging sorted arrays, and sliding window problems.

The technique can drastically reduce time complexity compared to brute force.

## Examples
Remove duplicates from sorted array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must also return the new length of the array.

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5 with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It doesn't matter what you leave beyond the returned length.

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Finding pairs in a sorted array that sum to a specific value.

## Key Concepts
- Two pointers move through data, often in opposite directions.  
- Efficient for sorted data.  
- Can be adapted for sliding windows and partitions.

## Summary
Mastering the two pointers technique optimizes solutions for many array and string problems, making code cleaner and faster.
