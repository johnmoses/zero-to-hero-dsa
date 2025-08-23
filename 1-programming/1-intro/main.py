"""
main.py

Python example code demonstrating basic programming concepts.
"""

def hello_world():
    print("Hello, World!")

def add_numbers(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    hello_world()
    print("Sum of 3 and 5:", add_numbers(3, 5))
    print("Factorial of 5:", factorial(5))
