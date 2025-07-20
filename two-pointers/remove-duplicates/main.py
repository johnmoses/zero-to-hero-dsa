""" 
Remove duplicates from sorted array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must also return the new length of the array.

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5 with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It doesn't matter what you leave beyond the returned length.

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

def remove_duplicates(nums):
    if not nums:
        return 0
    
    write_idx = 1
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    
    return write_idx

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))