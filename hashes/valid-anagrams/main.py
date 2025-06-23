""" 
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d1, d2 = {}, {}
    for i in range(len(s)):
        d1[s[i]] = 1 + d1.get(s[i], 0)
        d2[t[i]] = 1 + d2.get(t[i], 0)
    return d1 == d2
    
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))