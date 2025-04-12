"""
Reverse a String

Write a function that reverses a given string in-place.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
from typing import List

def reverseString1(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverseString2(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right -1
    print(s)

def reverseString3(s: List[str]) -> None:
    return s[::-1]

print(reverseString1(["h","e","l","l","o"]))
print(reverseString2(["h","e","l","l","o"]))
print(reverseString3(["h","e","l","l","o"]))