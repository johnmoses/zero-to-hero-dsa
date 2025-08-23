# Monotonic Queue - Python Example

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)

        if dq[0] == i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq])

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print("Sliding window maximum:", max_sliding_window(nums, k))
