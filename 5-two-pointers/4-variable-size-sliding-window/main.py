# Variable Size Sliding Window - Python Example

def min_subarray_len(target, arr):
    start = 0
    curr_sum = 0
    min_len = float('inf')
    
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return min_len if min_len != float('inf') else 0

arr = [2,3,1,2,4,3]
target = 7
print("Minimum subarray length with sum >= ", target, ":", min_subarray_len(target, arr))
