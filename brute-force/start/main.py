""" 
Brute Force.

Given an array of integers nums and an integer target, 
the goal is to find two indices in the array such that the corresponding elements add up to the target.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def find_pair_sums(nums: list[int], target: int) -> list[int]:
    # Loop through each number
    for i in range(len(nums)):
        # Check remaining numbers 
        for j in range(i + 1, len(nums)):
            # Return indices if sum equals target
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # Return empty list if no solution found        
    return []

def find_pair_sums1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(find_pair_sums([2, 7, 11, 15], 9))
print(find_pair_sums1([2, 7, 11, 15], 9))