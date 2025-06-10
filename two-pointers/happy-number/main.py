""" 
202. Happy Number
Easy

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false

Constraints:

1 <= n <= 231 - 1
"""

def isHappy(n: int) -> bool:
    def findSquareSum(num):
        _sum = 0
        while num > 0:
            n = num % 10  # first digit
            _sum += n**2
            num //= 10  # second digit
        return _sum

    # if the process doesnt lead to 1
    # well have an endless loop/cycle => slow and fast pointers
    s = f = n
    while True:
        s = findSquareSum(s)
        f = findSquareSum(findSquareSum(f))  # go two steps ahead
        if s == f:  # will catch up if cycle or if both are at 1
            break
    # check if happy number or not
    return s == 1
print(isHappy(19))