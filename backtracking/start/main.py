"""
Back tracking

Write a simple backtrack algorithm to find subsets of a set of numbers [1, 2, 3].
"""
def find_subsets(nums):
    result = []
    subset = []
    
    def backtrack(index):
        # Base case - add current subset copy to result 
        result.append(subset[:])
        
        # Try including each remaining element
        for i in range(index, len(nums)):
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
    
print(find_subsets([1, 2, 3]))
