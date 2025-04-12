""" 
Power
Performs exponentiation, similar to built-in pow() or ** feature
"""

def power(a: int, n: int, mod: int = None):
    """
    Iterative version of binary exponentiation

    Calculate a ^ n
    if mod is specified, return the result modulo mod

    Time Complexity :  O(log(n))
    Space Complexity : O(1)
    """
    ans = 1
    while n:
        if n & 1:
            ans = ans * a
        a = a * a
        if mod:
            ans %= mod
            a %= mod
        n >>= 1
    return ans

a = 2
n = 2
print(power(a,n))

def power_2(a, n, mod: int = None):
    if n == 0:
        ans = 1
    elif n == 1:
        ans = a
    else:
        ans = power_2(a, n//2, mod)
        ans = ans * ans
        if n % 2:
            ans = ans * a
    if mod: 
        ans %= mod
    return ans

print(power_2(a,n))