""" 
Factorial
1 = 1
2 = 1x2
3 = 1x2x3
4 = 1x2x3x4
"""

def factorial(n):
    assert n >= 0 and int(n) == n, 'n is positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print('Factorial: ', factorial(5))