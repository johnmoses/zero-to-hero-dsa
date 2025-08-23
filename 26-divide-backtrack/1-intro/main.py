# Divide and Conquer & Backtracking - Python example

# Divide and Conquer example: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Backtracking example: Simple subset sum checker
def subset_sum(nums, target, index=0):
    if target == 0:
        return True
    if target < 0 or index == len(nums):
        return False
    # Choose the current number
    if subset_sum(nums, target - nums[index], index + 1):
        return True
    # Skip the current number
    return subset_sum(nums, target, index + 1)

if __name__ == "__main__":
    arr = [3, 6, 1, 7, 2, 5]
    print("Sorted array:", merge_sort(arr))

    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print("Subset sum exists:", subset_sum(nums, target))
