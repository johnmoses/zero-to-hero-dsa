"""
Sorted squares
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order
"""

from typing import List

def sorted_squares(nums: List[int]) -> List[int]:
    """ 
    The keyword `sorted` is used to sort the results
    """
    return sorted(x*x for x in nums)

nums = [-4,-1,0,3,10]
print(sorted_squares(nums))