""" 
Fibonacci sequence with recursion
"""

n = 7

def fibonacci(n):
    if n <= 2:
        return [0, 1][:n]
    sequence = fibonacci(n-1)
    sequence.append(sum(sequence[-2:]))
    return sequence

print(fibonacci(n))