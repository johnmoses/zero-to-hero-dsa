""" 
Sentinel Search
"""
def sentinel_linear_search(arr, target):
    n = len(arr)
    arr.append(target)  # Append sentinel at the end
    
    i = 0
    while arr[i] != target:
        i += 1
    
    arr.pop()  # Remove sentinel
    
    if i < n:
        return i
    else:
        return "not found"

# Example usage
arr = [4, 2, 7, 1, 9, 5]
target = 7
result = sentinel_linear_search(arr, target)