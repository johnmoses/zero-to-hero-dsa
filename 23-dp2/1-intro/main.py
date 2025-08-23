# Advanced DP Intro - Python example
# Simple example showing DP applied to strings (Longest Palindromic Subsequence)

def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

if __name__ == "__main__":
    s = "bbbab"
    print(longest_palindromic_subseq(s))  # Output: 4
