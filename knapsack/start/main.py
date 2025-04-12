""" 
Knapsack algorithm

Write a basic knapsack algorithm. Give step by step explanation

The 0/1 Knapsack problem is a classic optimization problem where 
the goal is to maximize the total value of items that can be placed in a knapsack 
without exceeding the knapsack's capacity.

Example 1:
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)
"""

def knapsack(capacity, weights, values, n):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Args:
        capacity: The maximum weight capacity of the knapsack.
        weights: A list of the weights of the items.
        values: A list of the values of the items.
        n: The number of items.

    Returns:
        The maximum total value that can be put in the knapsack.
    """
    # Create a table to store results of subproblems
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


print(knapsack(50, [10, 20, 30], [60, 100, 120], 3))
