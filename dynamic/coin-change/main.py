""" 
Coin change with dynamic programming

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
def coin_change(coins, amount):
    # Initialize an array to store the minimum number of coins needed to make change for each amount
    dp = [float('inf')] * (amount + 1)

    # Base case: no coins needed to make change for amount 0
    dp[0] = 0

    # Iterate over the coins and amounts
    for coin in coins:
        # Update the minimum number of coins needed to make change for each amount
        for i in range(coin, amount + 1):
            # Update the minimum number of coins needed to make change for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1)
    # Return the minimum number of coins needed to make change for the target amount
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1,2,5], 11))