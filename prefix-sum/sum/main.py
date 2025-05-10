""" 
Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

Example:
Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3
Output: 9

Explanation:
Preprocess the array A to create a prefix sum array: P = [1, 3, 6, 10, 15, 21].
To find the sum between indices i and j, use the formula: P[j] - P[i-1].
"""
def sumRange(nums, i, j):
    P = [0] * (len(nums) + 1)
    for k in range(1, len(nums) + 1):
        P[k] = P[k - 1] + nums[k - 1]
    return P[j + 1] - P[i]

print(sumRange([1, 2, 3, 4, 5, 6], 1, 3))