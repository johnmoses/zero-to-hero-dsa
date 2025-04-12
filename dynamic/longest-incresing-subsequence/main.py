"""
Longest increasing non-contiguous sequence
"""

def longest_increasing_subsequence(sequence):
    # Define length and counts variables
    length = len(sequence)
    counts = [1 for _ in range(length)]

    # Iterate for length
    for i in range(1, length):
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                counts[i] = max(counts[i], counts[j] + 1)
    return max(counts)

print(longest_increasing_subsequence([1, 101, 10, 2, 3, 100, 4, 6, 2]))