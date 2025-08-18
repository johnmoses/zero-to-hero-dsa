"""
 Find the maximum value in an array by checking each element.

 Example 1:
 array = [3, 7, 2, 9, 5]
"""

def find_max(nums):
    """
    This is a brute force approach because it checks every element one by one without any shortcuts or optimizations. 
    The time complexity is O(n) where n is the number of elements
    """
    if not nums:
        return None  # or raise an error if empty list is invalid
    
    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([3, 7, 2, 9, 5]))
