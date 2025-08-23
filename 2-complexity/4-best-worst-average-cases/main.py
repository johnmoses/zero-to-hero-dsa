# Best, Worst, and Average Case - Python Example

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i  # found
    return -1  # not found

data = [1, 2, 3, 4, 5]

print("Best case (target=1):", linear_search(data, 1))    # O(1)
print("Worst case (target=6):", linear_search(data, 6))   # O(n)
print("Average case (target=3):", linear_search(data, 3)) # O(n)
