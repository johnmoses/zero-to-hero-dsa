# Interval Algorithms - Python example (Merge Intervals)

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals]

    for current in intervals[1:]:
        last = merged[-1]
        if current <= last:  # Overlapping intervals
            merged[-1] = (last, max(last, current))
        else:
            merged.append(current)

    return merged

if __name__ == "__main__":
    intervals = [(1,3), (2,6), (8,10), (15,18)]
    print(merge_intervals(intervals))  # Output: [(1, 6), (8, 10), (15, 18)]
