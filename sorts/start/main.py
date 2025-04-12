"""
Simple Sort Algorithm

Write a basic sort algorithm that takes a list of numbers and returns a sorted list.

Example 1:
    Input: [1, 5, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]

Example 2:
    Input: [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]
"""
def sort1(nums):
    """
    Sort a list of numbers in ascending order.

    Args:
        nums (list): A list of numbers to be sorted.

    Returns:
        list: A new list containing the sorted numbers.
    """
    return sorted(nums)
def sort2(nums):
    """
    Basic implementation of bubble sort algorithm
    Args:
        nums: List of numbers to sort
    Returns:
        Sorted list in ascending order
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(sort1([1, 5, 2, 3, 4]))
print(sort2([1, 5, 2, 3, 4]))
