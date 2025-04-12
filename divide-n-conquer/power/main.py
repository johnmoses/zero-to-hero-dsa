"""
Power
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    if (exponent==1):
        return (base)
    if(exponent!=1):
        return (base*power(base,exponent-1))
    
def power1(base, exponent):
    if exponent == 0:
        return 1
    return base * power1(base, exponent-1)

def powerSlow(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n-1)
    
def powerFast(x, n):
    if n == 0:
        return 1
    else:
        partial = power1(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(power(5,2))
print(powerSlow(5,2))
print(powerFast(5,2))
