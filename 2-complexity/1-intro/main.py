# Introduction to Complexity - Python Example

def linear_search(arr, target):
    # Simple search with linear time complexity O(n)
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Example usage
data = [4, 7, 1, 3, 9]
print("Index of 3:", linear_search(data, 3))
