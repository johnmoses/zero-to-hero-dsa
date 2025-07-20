""" 
Two Pointers.

Find two numbers in a sorted array that add up to a target value.

Example:
Input: nums = [1, 2, 3, 4, 6], target = 6
Output: [1, 3]

Explanation:
Initialize two pointers, one at the start (left) and one at the end (right) of the array.
Check the sum of the elements at the two pointers.
If the sum equals the target, return the indices.
If the sum is less than the target, move the left pointer to the right.
If the sum is greater than the target, move the right pointer to the left.
"""
def find_two_sum(nums: list[int], target: int) -> list[int]:
    # Use two pointers to find pair summing to target
    left, right = 0, len(nums) - 1
    
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
            
    return []  # No solution found

def find_two_sum2(nums: list[int], target:int) -> list[int]:
    left, right = 0, len(nums) -1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

def find_two_sum3(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

print(find_two_sum([1, 2, 3, 4, 6], 6))
print(find_two_sum2([1, 2, 3, 4, 6], 6))
print(find_two_sum3([1, 2, 3, 4, 6], 6))