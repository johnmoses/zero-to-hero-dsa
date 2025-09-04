# String DP - Python example (Edit Distance)

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the DP table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                   dp[i][j - 1],      # Insert
                                   dp[i - 1][j - 1])  # Replace
    return dp[m][n]

if __name__ == "__main__":
    w1 = "horse"
    w2 = "ros"
    print(edit_distance(w1, w2))  # Output: 3
