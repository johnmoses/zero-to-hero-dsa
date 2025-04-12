"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""

nums = [1,2,3,4,5,6,7]
k = 3

def rotate1(nums, k):
    """
    Do not return anything, modify aray in-place
    """
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a
    print(a)

rotate1(nums, k)

def rotate2(nums, k):
    if nums is None:
        return None

    n = len(nums)
    k = k % n
    return nums[n - k:] + nums[:n - k]

print(rotate2(nums,k))