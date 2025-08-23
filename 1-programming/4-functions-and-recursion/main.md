# Functions and Recursion

## Introduction
Functions are reusable blocks of code designed to perform specific tasks. Recursion is when a function calls itself to solve smaller instances of a problem.

## Details
Functions allow modular, organized code with inputs (parameters) and outputs (return values).

Recursion involves a base case to end the self-calls and a recursive case for continued processing. Recursion can simplify complex problems by breaking them down.

## Examples
Function example:

# Python
def greet(name):
    return "Hello, " + name + "!"

Recursion example for factorial:

def factorial(n):
    if n == 0:
        return 1  # base case
    else:
        return n * factorial(n-1)  # recursive case

## Key Concepts
- Functions encapsulate reusable code blocks.  
- Parameters and return values pass data in/out.  
- Recursion solves problems using self-calls.  
- Base case stops recursion to avoid infinite loops.

## Summary
Understanding functions and recursion is crucial for writing clean, efficient, and elegant programs that solve complex problems by breaking them down.
