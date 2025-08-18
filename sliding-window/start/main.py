""" 
Find Minimum Sum of SubArray of Size K

Input: arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
Output: 11
"""
def findMinSubarraySum(arr, k):
    curr_sum = 0
    min_sum = float("inf")
    start = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if (i - start + 1 == k):
            min_sum = min(min_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    
    return min_sum

def findMinSubarraySum1(arr, k):
    # Handle edge cases
    if not arr or k > len(arr):
        return 0
    
    # Calculate sum of first k elements
    curr_sum = sum(arr[:k])
    min_sum = curr_sum
    
    # Slide window and track min sum
    for i in range(k, len(arr)):
        curr_sum = curr_sum + arr[i] - arr[i-k]
        min_sum = min(min_sum, curr_sum)
        
    return min_sum


print(findMinSubarraySum([10, 4, 2, 5, 6, 3, 8, 1], 3))
print(findMinSubarraySum1([10, 4, 2, 5, 6, 3, 8, 1], 3))