# Common Hashing Problems - Python Example

from collections import Counter

# Anagram check
def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print("Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))

# Intersection of arrays
def array_intersection(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x in set1]

print("Intersection:", array_intersection([1,2,2,1], [2,2]))

# Two-sum problem
def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[num] = i
    return None

print("Two sum indices:", two_sum([2,7,11,15], 9))
