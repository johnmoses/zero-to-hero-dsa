"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""

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

rotate1([1,2,3,4,5,6,7], 3)