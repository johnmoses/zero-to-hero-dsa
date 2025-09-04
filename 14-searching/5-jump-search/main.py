""" 
Jump Search
"""
import math

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 55

def jump_search(arr, target):
    n = len(arr)
    m = int(math.sqrt(n))  # Block size to be jumped
    prev, curr = 0, 0
    
    # Jump ahead to find the block where the element may be present
    while curr < n and arr[curr] < target:
        prev = curr
        curr += m
        if curr >= n:
            curr = n
    
    # Perform a linear search in the identified block
    for i in range(prev, min(curr, n)):
        if arr[i] == target:
            return i
    
    return -1

print(jump_search(arr, target))