# Cumulative Sums - Python Example

def cumulative_count_positive(arr):
    cum_count = [0] * len(arr)
    cum_count = 1 if arr > 0 else 0
    for i in range(1, len(arr)):
        cum_count[i] = cum_count[i - 1] + (1 if arr[i] > 0 else 0)
    return cum_count

arr = [-1, 4, 2, -3, 5]
count_pos = cumulative_count_positive(arr)
# print("Cumulative count of positives:", count_pos)
