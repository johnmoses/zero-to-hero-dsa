""" 
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List


def canJump(nums: List[int]) -> bool:

    # Initialize the goal index to the last index of the list
    goal = len(nums) - 1

    # Iterate through the list from right to left
    for i in range(len(nums) - 1, -1, -1):
        # If the current index plus its jump length is greater than or equal to the goal index,
        # update the goal index to the current index
        if i + nums[i] >= goal:
            goal = i

    # If the goal index is 0, it means we can reach the last index
    return goal == 0


print(canJump([2, 3, 1, 1, 4]))
