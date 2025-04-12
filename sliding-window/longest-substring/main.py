""" 
Find Length of the Longest Substring That Doesn’t Contain Any Vowels

Input: s = "codeforintelligents"
Output: 3
Explanation: 'nts' is the longest substring that doesn't contain any vowels.
"""
def findLongestSubstring1(s):
    vowels = set('aeiou')
    longest = 0
    current = 0
    for char in s:
        if char in vowels:
            current = 0
        else:
            current += 1
            longest = max(longest, current)
    return longest

print(findLongestSubstring1("codeforintelligents"))


def findLongestSubstring2(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    maxResult = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
            print(result)
            if len(result) > len(maxResult):
                maxResult = result
        else:
            result = ""
    
    return len(maxResult)

print(findLongestSubstring2("codeforintelligents"))