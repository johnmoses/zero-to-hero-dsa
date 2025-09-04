# Variable Size Sliding Window

## Introduction
Variable size sliding window allows the window to expand or contract based on conditions, providing flexible coverage of the data.

## Details
Useful when the size of the subarray or substring to analyze depends on dynamic constraints, such as sums or character counts.

It adapts by moving the end pointer to grow and the start pointer to shrink the window.

## Examples
Finding the smallest subarray with a sum greater than or equal to a target.

Example:
Input: arr = [2,3,1,2,4,3], target = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length of 2.

## Key Concepts
- Window size adjusts during traversal.  
- Two pointers maintain window boundaries.  
- Effective for problems with dynamic constraints.

## Summary
Variable size sliding window handles complex variable length window problems efficiently by dynamically adjusting the window.
