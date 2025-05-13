""" 
Calculate the n-th Fibonacci number.

Example:
Input: n = 5
Output: 5 (The first five Fibonacci numbers are 0, 1, 1, 2, 3, 5)

Explanation:
Use a bottom-up approach to calculate the n-th Fibonacci number.
Start with the first two numbers (0 and 1) and iterate to calculate the next numbers like (dp[i] = dp[i - 1] + dp[i - 2]).
"""
def fibonacci(n: int) -> int:
    # Handle edge cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    # Initialize first two numbers
    dp = [0] * (n + 1)
    dp[1] = 1
    
    # Calculate fibonacci numbers bottom up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

print(fibonacci(5))