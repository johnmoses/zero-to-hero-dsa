""" 
Find Minimum Sum SubArray of Size K

Input: arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
Output: 11
"""
def findMinSum1(arr, k):
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

def findMinSum2(arr, k):
    currSum = 0
    minSum = float("inf")
    start = 0
    
    for i in range(len(arr)):
        currSum += arr[i]
        
        if (i - start + 1 == k):
            minSum = min(minSum, currSum)
            currSum -= arr[start]
            start += 1
    
    return minSum

print(findMinSum1([10, 4, 2, 5, 6, 3, 8, 1], 3))
print(findMinSum2([10, 4, 2, 5, 6, 3, 8, 1], 3))