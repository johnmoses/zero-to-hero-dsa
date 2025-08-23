# 1D DP Patterns - Python example (Climbing Stairs)

def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp, dp = 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":
    print(climb_stairs(10))  # Output: 89
