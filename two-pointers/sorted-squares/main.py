""" 
Two Pointers.

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
def sorted_squares(nums):
    # Create result array to store squares
    result = [0] * len(nums)
    
    # Two pointers - start and end of array
    left = 0
    right = len(nums) - 1
    idx = len(nums) - 1
    
    # Compare absolute values from both ends and place squares
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[idx] = nums[left] * nums[left]
            left += 1
        else:
            result[idx] = nums[right] * nums[right]
            right -= 1
        idx -= 1
            
    return result

print(sorted_squares([-4,-1,0,3,10]))