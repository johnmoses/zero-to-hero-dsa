""" 
Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Example 1:

Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Constraints:

1 <= n <= 231 - 1
 
Follow up: If this function is called many times, how would you optimize it?
Seen this question in a real interview before?
1/5
"""


def numberOfBits(n: int) -> int:
    count = 0
    while n:
        count += n % 2
        n = n >> 1
    return count

print(numberOfBits(11))