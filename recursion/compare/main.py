""" 
Recursion vs Iteration
"""

def powerOfTwoRecursion(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwoRecursion(n-1)
        return power * 2
print('Power of Two Recursion: ', powerOfTwoRecursion(3))

def powerOftwoIteration(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

print('Power of Two iteration: ', powerOftwoIteration(3))