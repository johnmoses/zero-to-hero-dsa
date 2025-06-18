""" 
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
def containsDuplicate(nums):
    duplicated = set(nums)
    if len(duplicated) < len(nums):
        return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))