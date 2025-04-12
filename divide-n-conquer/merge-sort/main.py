""" 
Write a divide and conquer function for merge sort

Example 1
Input: nums = [7,1,5,3,6,4]
Output: [1,3,4,5,6,7]

Example 2
Input: nums = [1]
Output: [1]
"""
def mergeSotr1(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSotr1(arr[:mid])
    right = mergeSotr1(arr[mid:])
    return merge1(left, right)

def merge1(left, right):
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


def mergeSort2(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = mergeSort2(nums[0:pivot])
    right_list = mergeSort2(nums[pivot:])
    return merge2(left_list, right_list)


def merge2(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    
    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    
    return ret

print(mergeSotr1([7,1,5,3,6,4]))
print(mergeSort2([7, 1, 5, 3, 6, 4]))