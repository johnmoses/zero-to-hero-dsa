# Tabulation - Python example

def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":
    print(fib(10))  # Output: 55
