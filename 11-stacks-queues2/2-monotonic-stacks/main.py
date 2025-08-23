# Monotonic Stack - Python Example

def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)
    return result

arr = [2, 1, 2, 4, 3]
print("Next greater elements:", next_greater_elements(arr))
