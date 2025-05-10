""" 
Find an element in a rotated sorted array.

Example:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Explanation:
Perform binary search with an additional check to determine which half of the array is sorted.
We then check if the target is within the range of the sorted half.
If it is, we search that half; otherwise, we search the other half.
"""
def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        # Right half is sorted        
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1 
            else:
                right = mid - 1
                
    return -1

print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))