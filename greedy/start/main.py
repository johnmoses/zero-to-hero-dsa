"""
Greedy programming

Write a basic greedy programming algorithm to find the minimum number of coins required to make change for a given amount of money.
The coins available are 1, 5, and 10 cents.

Note: You can assume that the input amount will always be a positive integer.
Steps are
    1. Initialize an empty list to store the coins.
    2. Loop until the amount becomes zero.
    3. If the amount is greater than or equal to 10 cents, add a 10 cent coin and subtract 10 cents from the amount.
    4. If the amount is greater than or equal to 5 cents, add a 5 cent coin and subtract 5 cents from the amount.
    5. If the amount is greater than or equal to 1 cent, add a 1 cent coin and subtract 1 cent from the amount.
    6. Return the list of coins.
"""

def greedy_change(amount):
    # Initialize an empty list to store the coins
    coins = []
    
    # Loop until the amount becomes zero
    while amount > 0:
        # If the amount is greater than or equal to 10 cents, add a 10 cent coin
        if amount >= 10:
            coins.append(10)
            amount -= 10
        # If the amount is greater than or equal to 5 cents, add a 5 cent coin
        elif amount >= 5:
            coins.append(5)
            amount -= 5
        # If the amount is greater than or equal to 1 cent, add a 1 cent coin
        elif amount >= 1:
            coins.append(1)
            amount -= 1
    
    # Return the list of coins
    return coins


print(greedy_change(28))  # Output: [10, 10, 5, 1, 1, 1]
