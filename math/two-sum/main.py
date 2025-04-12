"""
Two Sum
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    # Define a dictionary
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return dic[num], i 
        else:
            dic[target - num] = i
    return None

print(two_sum(nums, target))