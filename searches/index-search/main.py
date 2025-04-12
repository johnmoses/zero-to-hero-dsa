""" 
Search Algorithm
Searching for the index of a selected number
"""
from typing import List

nums = [-1,0,3,5,9,12]
target = 9


def search_1(nums: int, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        current_num = nums[mid]
        if current_num == target:
            return mid
        elif target < current_num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def search_2(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

print(search_1(nums, target))
print(search_2(nums, target))