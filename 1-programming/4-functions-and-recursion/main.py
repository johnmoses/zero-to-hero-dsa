# 4 Functions And Recursion - Python example

def greet(name):
    print("Hello, " + name)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

greet("Alice")
print("Factorial of 5:", factorial(5))
