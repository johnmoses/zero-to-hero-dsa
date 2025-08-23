# Monotonic Stack - Python example (Next Greater Element)

def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result

if __name__ == "__main__":
    nums = [2, 1, 2, 4, 3]
    print(next_greater_elements(nums))  # Output: [4, 2, 4, -1, -1]
