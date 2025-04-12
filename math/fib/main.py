"""
Fibonnacci
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

n = 2
sn = Solution()
print(sn.fib(n))