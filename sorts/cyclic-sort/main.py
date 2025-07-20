""" 
Cyclic sort

Given an array, [5, 3, 6, 2, 10], write a cyclic sort algorithm to sort the array in ascending order.
The output should be [2, 3, 5, 6, 10]
"""
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1

def find_missing_number(nums):
    n = len(nums)
    i = 0
    
    while i < n:
        if nums[i] < n and nums[i] != nums[nums[i]]:
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n

def find_all_missing(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)
    
    return missing

# print(find_all_missing([5, 3, 6, 2, 10]))
# print(find_missing_number([5, 3, 6, 2, 10]))
# print(cyclic_sort([5, 3, 6, 2, 10]))