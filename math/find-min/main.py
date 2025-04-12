# Find maximum number

numbers = [2, 4, 5, 6, 9, 34, 20, 2]

def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

print(find_min(numbers))