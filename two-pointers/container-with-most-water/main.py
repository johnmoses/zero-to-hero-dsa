""" 
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List


def maxArea(height: List[int]) -> int:
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    if n == 2:
        return min(height[0], height[1])
    else:
        left = 0
        right = n - 1
        clh = 0
        crh = 0
        mx = 0
        while left < right:

            if height[left] < height[right]:
                mx = max(height[left] * (right - left), mx)
                clh = height[left]
                while height[left] <= clh:
                    left += 1
                    if left >= right:
                        return mx

            else:
                mx = max(height[right] * (right - left), mx)
                crh = height[right]
                while height[right] <= crh:
                    right -= 1
                    if left >= right:
                        return mx
        return mx


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
