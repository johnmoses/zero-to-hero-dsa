"""
Simple Algorithm to demonstrate big o
"""
def demonstrate_constant_time(arr):
    """O(1) - Constant Time"""
    return arr[0] if arr else None

def demonstrate_linear_time(arr):
    """O(n) - Linear Time"""
    total = 0
    for num in arr:
        total += num
    return total

def demonstrate_quadratic_time(arr):
    """O(n^2) - Quadratic Time"""
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(demonstrate_constant_time([1, 2, 3, 4, 5]))
print(demonstrate_linear_time([1, 2, 3, 4, 5]))
print(demonstrate_quadratic_time([5, 4, 3, 2, 1]))