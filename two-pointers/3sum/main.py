""" 
# 15. 3Sum

Medium

Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Example 1:
    
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Constraints:
    
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Sort the list
    nums.sort()
    # Define results array
    res = []
    # Traverse the nums list
    for i in range(len(nums)):
        # Check if i is greater than zero and that value at i is equal to value of previous index
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Get lowest and highest index
        lo, hi = i + 1, len(nums) - 1
        # Loop through each item from low index to high index
        while lo < hi:
            threeSum = nums[i] + nums[lo] + nums[hi]
            if threeSum > 0:
                hi -= 1
            elif threeSum < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                while nums[lo] == nums[lo - 1] and lo < hi:
                    lo += 1
    return res

def threeSum1(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            cursum = nums[i] + nums[lo] + nums[hi]
            if cursum < 0:
                lo += 1
            elif cursum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                while nums[lo] == nums[lo-1] and lo < hi:
                    lo += 1
    return res
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum1([-1,0,1,2,-1,-4]))