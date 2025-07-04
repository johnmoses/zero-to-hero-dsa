"""
Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
def subsets(nums):
    result = []
    subset = []
    
    def backtrack(start):
        # Base case - add current subset copy to result 
        result.append(nums[:])
        
        # Try including each remaining element
        for i in range(start, len(nums)):
            # Add the element
            subset.append(nums[i])
            # Move onto the next element
            backtrack(i + 1)
            # Remove the element
            subset.pop()
    # Start at the first element of the array
    backtrack(0)
    # Return the result
    return result


def subsets2(nums):
    result = []
    subset = []
    def backtrack(start):
        result.append(nums[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
    backtrack(0)
    return result
    
print(subsets([1, 2, 3]))
print(subsets2([1, 2, 3]))
