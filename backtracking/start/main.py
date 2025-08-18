""" 
Generate all permutations of a given list of numbers.

Example:
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Explanation:
Use recursion to generate permutations.
For each element, include it in the current permutation and recursively generate the remaining permutations.
Backtrack when all permutations for a given path are generated.
"""
from typing import List

def permute(nums: list) -> List[List[int]]:
    # Define result array
    result = []
    def backtrack(start):
        # Base case: add all elements to result if number of elements is not zero
        if start == len(nums):
            result.append(nums[:])
            return
        # Iterate and include each element
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            # Move to next element
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    # Start at first element of array
    backtrack(0)
    # Return result
    return result


print(permute([1, 2, 3]))
