"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""

def rotate(nums, k):
    """
    Do not return anything, modify aray in-place
    """
    n = len(nums)
    arr = [0] * n
    for i in range(n):
        arr[(i + k) % n] = nums[i]

    nums[:] = arr
    print(arr)


rotate([1,2,3,4,5,6,7], 3)