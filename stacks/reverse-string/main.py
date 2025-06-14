"""
Write a Function that can reverse a string using stack data structure
"""
def reverseString1(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

print(reverseString1("MAPS"))
