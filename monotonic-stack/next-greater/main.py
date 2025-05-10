""" 
Find the next greater element for each element in an array. Output -1 if the greater element doesn’t exist.

Example:
Input: nums = [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]

Explanation:
Use a stack to keep track of elements for which we haven’t found the next greater element yet.
Iterate through the array, and for each element, pop elements from the stack until you find a greater element.
If the stack is not empty, set the result for index at the top of the stack to current element.
Push the current element onto the stack.
"""
def find_next_greater(nums):
    # Initialize result array with -1 as default value
    result = [-1] * len(nums)
    stack = []

    # Iterate through array and find next greater element
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = nums[i]
        stack.append(i)
        
    return result