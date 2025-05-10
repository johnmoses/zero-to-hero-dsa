""" 
Problem Statement: Merge all overlapping intervals.

Example:
Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]

Explanation:
Sort the intervals by their start time.
Create an empty list called merged to store the merged intervals.
Iterate through the intervals and check if it overlaps with the last interval in the merged list.
If it overlaps, merge the intervals by updating the end time of the last interval in merged.
If it does not overlap, simply add the current interval to the merged list.
"""
def merge_intervals(intervals):
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize merged list with first interval
    merged = [intervals[0]] if intervals else []
    
    # Merge overlapping intervals
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1]) 
        else:
            merged.append(interval)

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))