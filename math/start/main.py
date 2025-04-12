""" 
Math algorithms

Write code to demonstrate basic math operations in Python
"""
def add_numbers(a, b):
    """Add two numbers"""
    return a + b

print('Add numbers: ', add_numbers(1, 2))

def subtract_numbers(a, b): 
    """Subtract two numbers"""
    return a - b

print('Subtract numbers: ', subtract_numbers(1, 2))

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

print('Multiply numbers: ', multiply_numbers(1, 2))

def divide_numbers(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b

print('Divide numbers: ', divide_numbers(1, 2))

def modulo_numbers(a, b):
    """Get remainder of division"""
    return a % b

print('Modulo numbers: ', modulo_numbers(1, 2))

def power_of_number(base, exponent):
    """Calculate power of a number"""
    return base ** exponent

print('Power of number: ', power_of_number(2, 3))

def absolute_value(number):
    """Get absolute value"""
    return abs(number)

print('Absolute value: ', absolute_value(-2))

def round_number(number, decimals=0):
    """Round a number to specified decimal places"""
    return round(number, decimals)

print('Round number: ', round_number(1.23456, 2))

def floor_division(a, b):
    """Integer division discarding remainder"""
    return a // b

print('Floor division: ', floor_division(5, 2))

def ceil_division(a, b):
    """Integer division rounding up"""
    return (a + b - 1) // b

print('Ceil division: ', ceil_division(5, 2))

def gcd(a, b):
    """Greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

print('GCD: ', gcd(12, 18))

def lcm(a, b):
    """Least common multiple"""
    return a * b // gcd(a, b)

print('LCM: ', lcm(12, 18))

def factorial(n):
    """Factorial of a number"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print('Factorial: ', factorial(5))

def fibonacci(n):
    """Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print('Fibonacci: ', fibonacci(5))

def is_even(n):
    """Check if a number is even"""
    return n % 2 == 0

print('Is even: ', is_even(2))

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print('Is prime: ', is_prime(7))

def is_palindrome(s):
    """Check if a string is a palindrome"""
    return s == s[::-1]

print('Is palindrome: ', is_palindrome('racecar'))

def is_armstrong(n):
    """Check if a number is an Armstrong number"""
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

print

def is_perfect_square(n):
    """Check if a number is a perfect square"""
    return int(n ** 0.5) ** 2 == n

print('Is perfect square: ', is_perfect_square(16))

def is_perfect_number(n):
    """Check if a number is a perfect number"""
    return sum(i for i in range(1, n) if n % i == 0) == n

print('Is perfect number: ', is_perfect_number(28))

def is_perfect_cube(n):
    """Check if a number is a perfect cube"""
    return int(n ** (1/3)) ** 3 == n

print('Is perfect cube: ', is_perfect_cube(27))