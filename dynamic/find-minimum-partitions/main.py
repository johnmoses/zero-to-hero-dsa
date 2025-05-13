""" 
Given a string s, partition s such that every substring of the
partition is a palindrome.
Find the minimum cuts needed for a palindrome partitioning of s.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

def find_minimum_partitions(string: str) -> int:
    # Initialize values
    length = len(string)
    cut = [0] * length
    is_palindrome = [[False for i in range(length)] for j in range(length)]

    # Iterate over string
    for i, c in enumerate(string):
        # Check for palindromes
        minicut = i
        for j in range(i + 1):
            if c == string[j] and (i - j < 2 or is_palindrome[j+1][i-1]):
                # Found a palindrome
                is_palindrome[j][j] = True
                minicut = min(minicut, 0 if j == 0 else (cut[j-1] + 1))
        cut[i] = minicut
    return cut[length-1]

s = 'get'
print(find_minimum_partitions(s)) 