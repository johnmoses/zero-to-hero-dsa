"""
Wiggle sort

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
"""
def wiggleSort1(nums):
    """
    Rearrange array such that nums[0] < nums[1] > nums[2] < nums[3]...
    """
    # Sort array first 
    nums.sort()
    
    # Swap adjacent elements starting from index 1
    for i in range(1, len(nums)-1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums


def wiggleSort2(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]
    return nums

print(wiggleSort1([3,5,2,1,6,4]))
print(wiggleSort2([3,5,2,1,6,4]))