"""
Simple  Bubble Sort Algorithm

Write a basic sort algorithm that takes a list of numbers and returns a sorted list.

Example 1:
    Input: [1, 5, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]

Example 2:
    Input: [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]
"""
def sort1(nums):
    return sorted(nums)
    
def sort2(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def sort3(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(sort1([1, 5, 2, 3, 4]))
print(sort2([1, 5, 2, 3, 4]))
print(sort3([1, 5, 2, 3, 4]))

