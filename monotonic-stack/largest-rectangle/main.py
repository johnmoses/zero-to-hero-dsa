""" 
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
def largest_rectangle_area(heights):
    """Find the area of largest rectangle in histogram."""
    if not heights:
        return 0
        
    stack = []
    max_area = 0
    heights.append(0) # Add dummy bar to process remaining bars

    for i in range(len(heights)):
        start = i
        
        while stack and stack[-1][1] > heights[i]:
            index, height = stack.pop()
            width = i - index
            max_area = max(max_area, width * height)
            start = index
            
        stack.append((start, heights[i]))
        
    return max_area

print(largest_rectangle_area([2,1,5,6,2,3]))