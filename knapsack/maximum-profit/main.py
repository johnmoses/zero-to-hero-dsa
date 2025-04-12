
"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
no_of_items 4
profit 5 4 8 6
weight 1 2 4 5
max_weight 5
Constraints:
max_weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the maximum profit that the shopkeeper can make given maxmum weight that can
be carried.
"""
weights = [3 ,4 , 5]
values = [10, 9 , 8]
number_of_items = 3
max_weight = 25
index = 0

def knapsack(
    weights: list,
    values: list,
    number_of_items: int,
    max_weight: int,
    index: int
) -> int:
    if index == number_of_items:
        return 0
    # Initialize variables
    ans1 = 0
    ans2 = 0
    ans1 = knapsack(weights, values, number_of_items, max_weight, index + 1)
    if weights[index] <= max_weight:
        ans2 = values[index] + knapsack(
            weights, values, number_of_items, max_weight - weights[index], index + 1
        )
    return max(ans1, ans2)

print(knapsack(weights, values, number_of_items, max_weight, index))
# 27