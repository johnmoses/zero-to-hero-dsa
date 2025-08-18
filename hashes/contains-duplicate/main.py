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


def containsDuplicate(nums: List[int]) -> bool:
    # Create a set from the list to clean-up duplicate entries
    cleaned = set(nums)
    # Check if length of cleaned is less than length of original 
    if len(cleaned) < len(nums):
        return True
    return False

print(containsDuplicate([1, 2, 3, 1]))
