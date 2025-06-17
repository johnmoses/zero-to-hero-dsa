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
def generate_permutations(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            
    backtrack(0)
    return result

print(generate_permutations([1, 2, 3]))