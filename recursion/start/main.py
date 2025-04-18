""" 
Recursion

Write a simple recursion algorithm
to print numbers from 1 to n in normal order and then print numbers from n to 1 in reverse order.
"""

# Numbers in normal order
def recursion1(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursion1(n-1)
        print(n)

# Numbers in reverse order
def recursion2(n):
    if n < 1:
        return
    else:
        print(n)
        recursion2(n-1)

print('recursion1(5) = ', recursion1(5))
print('recursion2(5) = ', recursion2(5))