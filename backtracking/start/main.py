"""
Back tracking

Write a simple backtrack algorithm to find subsets of a set.
"""
def get_subsets(nums):
    """Find all subsets of the input array using backtracking"""
    result = []
    subset = []
    
    def backtrack(index):
        # Base case - add current subset copy to result
        result.append(subset[:])
        
        # Try including each remaining element
        for i in range(index, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
    backtrack(0)
    return result
    
print(get_subsets([1, 2, 3]))
