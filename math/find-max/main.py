# Find maximum number

numbers = [2, 4, 5, 6, 9, 34, 60, 20, 2]

def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(numbers))