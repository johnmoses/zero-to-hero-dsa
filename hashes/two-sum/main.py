""" 
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))