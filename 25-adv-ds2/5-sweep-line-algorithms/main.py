# Sweep Line Algorithms - Python example (Counting overlapping intervals)

def count_overlaps(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # 1 for interval start
        events.append((end, -1))    # -1 for interval end

    events.sort()
    active = 0
    max_overlaps = 0

    for _, event_type in events:
        active += event_type
        max_overlaps = max(max_overlaps, active)

    return max_overlaps

if __name__ == "__main__":
    intervals = [(1,3), (2,5), (4,6), (7,8)]
    print(count_overlaps(intervals))  # Output: 3
