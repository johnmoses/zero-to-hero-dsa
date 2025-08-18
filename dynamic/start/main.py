"""
Dynamic programming

Write a basic dynamic programming algorithm to solve the fibonacci problem explaining the steps.
"""
def fibonacci_dp(n):
    # Create array to store previously calculated fibonacci numbers
    fib = [0] * (n + 1)
    # print('fibs: ', fib)
    
    # Base cases
    fib[0] = 0
    fib[1] = 1
    
    # Build fibonacci numbers bottom up
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
        # Print the sequence
        print('fib: ',fib[i])
    # Return number at n
    return fib[n]

print(fibonacci_dp(10))