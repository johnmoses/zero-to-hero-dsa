""" 
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Create a dictionary to store the frequency of each element
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Create a list of tuples (frequency, element) and sort it in descending order
    freq_list = sorted([(v, k) for k, v in freq.items()], reverse=True)

    # Return the top k elements
    return [freq_list[i][1] for i in range(k)]

print(topKFrequent([1,1,1,2,2,3], 2))