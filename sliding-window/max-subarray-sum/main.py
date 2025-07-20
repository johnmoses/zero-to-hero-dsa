""" 
Find the maximum sum of a subarray of size k.

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9

Explanation:
Start with the sum of the first k elements.
Slide the window one element at a time, subtracting the element that goes out of the window and adding the new element.
Keep track of the maximum sum encountered.
"""
def find_max_subarray_sum(nums, k):
    # Handle invalid input
    if not nums or k <= 0 or k > len(nums):
        return 0
        
    # Calculate sum of first window
    window_sum = sum(nums[:k]) 
    max_sum = window_sum
    
    # Slide window and track max sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

def find_max_subarray_sum1(nums, k):
    if len(nums) < k:
        return -1
    
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(find_max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
print(find_max_subarray_sum1([2, 1, 5, 1, 3, 2], 3))