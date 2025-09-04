# Time and Space Complexity - Python Example

def sum_list(items):
    total = 0              # O(1) space for total
    for item in items:     # O(n) time for loop
        total += item
    return total

def copy_list(items):
    new_list = []          # O(n) space
    for item in items:     # O(n) time
        new_list.append(item)
    return new_list

print("Sum of list:", sum_list([1, 2, 3, 4, 5]))  # Output: 15
print("Copy of list:", copy_list([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4,