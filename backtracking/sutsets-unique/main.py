""" 
Given a collection of integers that might contain duplicates, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

Example:
    Input: [1,2,2]
    Output: [(1, 2), (2,), (1,), (1, 2, 2), (2, 2), ()]
"""

def subsetsUnique(nums):
    
    def backtrack(res, nums, stack, pos):
        if pos == len(nums):
            res.add(tuple(stack))
        else:
            # take
            stack.append(nums[pos])
            backtrack(res, nums, stack, pos+1)
            stack.pop()

            # don't take
            backtrack(res, nums, stack, pos+1)

    res = set()
    backtrack(res, nums, [], 0)
    return list(res)

print(subsetsUnique([1,2,2]))