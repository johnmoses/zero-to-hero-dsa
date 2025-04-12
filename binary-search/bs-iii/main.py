""" 
Template III

Example 1:
    
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
"""
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: 
        return left
    if nums[right] == target: 
        return right
    return -1

print(binarySearch([-1,0,3,5,9,12], 9))