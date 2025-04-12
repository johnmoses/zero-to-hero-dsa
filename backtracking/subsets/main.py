''' 
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[ [] [1] [2] [1, 2] [3] [1, 3] [2, 3] [1, 2, 3] ]
'''

# Using iteration
def subsets(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res

print(subsets([1, 2, 3]))