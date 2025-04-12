"""
Dynamic programming

Write a basic dynamic programming algorithm to solve the fibonacci problem explaining the steps.
"""
def fibonacci_dp(n):
    # Create array to store previously calculated fibonacci numbers
    fib = [0] * (n + 1)
    
    # Base cases
    fib[0] = 0
    fib[1] = 1
    
    # Build fibonacci numbers bottom up
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
        
    return fib[n]

def fibonacci_optimized(n):
    # Use only two variables to optimize space
    if n <= 1:
        return n
        
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
        
    return curr

print(fibonacci_dp(10))
print(fibonacci_optimized(10))