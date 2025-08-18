"""
Power
"""

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

def powerSlow(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
def powerFast(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(power(5,2))
print(powerSlow(5,2))
print(powerFast(5,2))
