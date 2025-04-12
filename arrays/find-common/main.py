""" 
Find common elements in two arrays.
"""

def find_common(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(find_common([1,2,3,4,5], [4,5,6,7,8]))