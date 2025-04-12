""" 
Fibonacci numbers, commonly denoted Fn, is a sequence such that
each number is the sum of the two preceeding ones starting from 0 and 1
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Here is an example 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….
"""

def fibonacci(n):
    # Set preconditions
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print('Fibonacci: ', fibonacci(3))
# Sequence
print([fibonacci(n) for n in range(5)])
