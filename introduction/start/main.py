"""
A Simple Algorithm:
    
Fibonacci numbers using native approach

Fibonacci numbers is a sequence such that
each number is the sum of the two preceeding ones starting from 0 and 1
So we have 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

prev1 = 0
prev2 = 1
next_number = prev2  
count = 1
print(prev1, end=" ")
print(prev2, end=" ")

while count <= 5:
    print(next_number, end=" ")
    count += 1
    prev1, prev2 = prev2, next_number
    next_number = prev1 + prev2
print()