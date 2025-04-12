""" 
Fibonacci Search
""" 

def fibonacci_search(arr, target):
    n = len(arr)
    fib_k2, fib_k1 = 0, 1
    
    # Generate Fibonacci numbers
    while fib_k1 < n:
        fib_k2, fib_k1 = fib_k1, fib_k1 + fib_k2
    
    left, right = 0, n - 1
    
    while fib_k1 > 1:
        mid = left + fib_k2 - 1
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
            fib_k2, fib_k1 = fib_k1, fib_k1 - fib_k2
        else:
            right = mid - 1
            fib_k1, fib_k2 = fib_k2, fib_k1 - fib_k2
    
    if left <= right and arr[left] == target:
        return left
    
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
print(fibonacci_search(arr))