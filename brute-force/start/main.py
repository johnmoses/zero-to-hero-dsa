""" 
Brute Force.

Given an array of integers nums and an integer target, 
the goal is to find two indices in the array such that the corresponding elements add up to the target.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def two_sum(nums, target):
    """
    The time complexity is O(n²) because for each element we check all subsequent elements. 
    The space complexity is O(1) because we only use a few extra variables.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(two_sum([2, 7, 11, 15], 9))