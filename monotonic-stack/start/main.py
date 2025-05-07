""" 
Monotonic Stacks.

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
def next_greater_elements(nums):
    # Initialize result array with -1
    n = len(nums)
    result = [-1] * n
    stack = []

    # Search two times to handle circular array
    for i in range(2*n):
        # Get the actual index for circular array
        curr_idx = i % n
        
        # Process stack while curr number is greater
        while stack and nums[stack[-1]] < nums[curr_idx]:
            idx = stack.pop()
            result[idx] = nums[curr_idx]
            
        if i < n:
            stack.append(curr_idx)
            
    return result

print(next_greater_elements([1,2,1]))
print(next_greater_elements([1, 2, 3, 4, 3]))