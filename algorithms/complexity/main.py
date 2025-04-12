"""
Algorithm Complexity Analysis

Write code to demonistrate algorithm complexity or efficiency
"""
lst = [1, 2, 3, 4, 5, 7, 8, 8, 8, 9, 11, 10, 14, 25]

def constant_time(lst):
    """O(1) - Constant time complexity"""
    return lst[0] if lst else None

print(constant_time(lst))

def linear_time(lst):
    """O(n) - Linear time complexity"""
    total = 0
    for item in lst:
        total += item
    return total

print(linear_time(lst))

def quadratic_time(lst):
    """O(n^2) - Quadratic time complexity"""

    pairs = []
    for i in lst:
        for j in lst:
            pairs.append((i,j))
    return pairs

print(quadratic_time(lst))

def binary_search(lst, target):
    """O(log n) - Logarithmic time complexity"""
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target: 
            return mid
        elif lst[mid] < target: 
            left = mid + 1
        else: 
            right = mid - 1

    return -1
print(binary_search(lst, 3))

def merge_sort(lst):
    """O(n log n) - Log-linear time complexity"""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid]) 
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort(lst))

def exponential_time(lst):
    """O(2^n) - Exponential time complexity"""
    if len(lst) == 0: 
        return []
    return [lst] + exponential_time(lst + lst)

print(exponential_time(lst))

def polynomial_time(lst):
    """O(n!) - Polynomial time complexity"""
    if len(lst) == 0: 
        return []
    return [lst] + polynomial_time(lst + lst)

print(polynomial_time(lst))

def factorial_time(lst):
    """O(n!) - Factorial time complexity"""
    if len(lst) == 0: 
        return []
    return [lst] + factorial_time(lst + lst)

print(factorial_time(lst))

def fibonacci_time(n):
    """O(2^n) - Fibonacci time complexity"""
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return fibonacci_time(n-1) + fibonacci_time(n-2)

print(fibonacci_time(3))
