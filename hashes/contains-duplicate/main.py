"""
Contains Duplicates

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicated = set(nums)
        if len(duplicated) < len(nums):
            return True
        return False

nums = [1,2,3,1]
sn = Solution()
print(sn.containsDuplicate(nums))