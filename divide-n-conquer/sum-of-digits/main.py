"""
Sum of Digits

Input: 222
Output: 6
"""

def sumofDigits(n):
    assert n>=0 and int(n) == n
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(222))