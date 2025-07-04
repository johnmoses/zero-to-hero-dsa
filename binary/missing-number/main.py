""" 
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for i in range(1, n + 1):
        res ^= i
    for num in nums:
        res ^= num
    return res

def missingNumber1(nums: List[int]) -> int:
    res, n = 0, len(nums)
    for i in range(1, n + 1):
        res ^= i
    for num in nums:
        res ^= num
    return res

print(missingNumber([3,0,1]))
print(missingNumber1([3,0,1]))