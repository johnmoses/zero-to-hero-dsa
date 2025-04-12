"""
Recursion

Write a simple recursion algorithm
to print numbers from 1 to n in reverse order.

"""
def recursion1(n):
    if n < 1:
        return
    else:
        print(n)
        recursion1(n-1)

""" 
Write a simple recursion algorithm
to print numbers from 1 to n in normal order
"""
def recursion2(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursion2(n-1)
        print(n)

print('recursion1(5) = ', recursion1(5))
print('recursion2(5) = ', recursion2(5))