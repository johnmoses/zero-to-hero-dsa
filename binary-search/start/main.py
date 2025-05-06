""" 
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
def binarySearch(nums: list[int], target: int) -> int:
    # Set the left pointer to 0
    left = 0
    # Set the right pointer to the length of the array minus 1
    right = len(nums) - 1
    # print('right: ', right)
    # Loop through the array until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        # print('mid: ',mid)
        # Check if the middle element is equal to the target
        if nums[mid] == target:
            # Return the index of the target
            return mid
        # Check if the middle element is less than the target
        elif nums[mid] < target:
            # Update the left pointer to the middle index + 1
            left = mid + 1
        else:
            # Update the right pointer to the middle index - 1
            right = mid - 1
            
    return -1

print(binarySearch([-1,0,3,5,9,12], 9))