# Common string problems
from typing import List

""" 
Compare two strings using list comprehension
"""
def compare_strings1(string1, string2):
    return [i for i in range(len(string1)) if string1[i] != string2[i]]

"""
Compare two strings using a for loop
"""
def compare_strings2(string1, string2):
    diff = []
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff.append(i)
    return diff

"""
Compare two strings using a while loop
"""
def compare_strings3(string1, string2):
    diff = []
    i = 0
    while i < len(string1):
        if string1[i] != string2[i]:
            diff.append(i)
        i += 1
    return diff

print(compare_strings1("Hello World", "Hella Warld"))
print(compare_strings2("Hello World", "Hella Warld"))
print(compare_strings3("Hello World", "Hella Warld"))

def reverseString1(s: List[str]) -> None:
    return s[::-1]

def reverseString2(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right -1
    print(s)

print(reverseString1(["h","e","l","l","o"]))
reverseString2(["h","e","l","l","o"])