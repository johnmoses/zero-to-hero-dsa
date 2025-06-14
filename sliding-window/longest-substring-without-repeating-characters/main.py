""" 
Longest Substring Without Repeating Characters

Hint
Given a string s, find the length of the longest 
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
"""
def lengthOfLongestSubstring(s: str) -> int:
    # Initialize set st, n as sliding wondow pointer, res to store result
    st = set()
    n = 0
    res = 0
    # Iterate through the string s with i as right pointer
    for i in range(len(s)):
        # Handle repeating character
        while s[i] in st:
            st.remove(s[n])
            n += 1
        # Add current character to set
        st.add(s[i])
        # Update result
        res = max(res, i - n + 1)
    # Return result
    return res

def lengthOfLongestSubstring1(s: str) -> int:
    st = set()
    n = 0
    res = 0
    for i in range(len(s)):
        while s[i] in st:
            st.remove(s[n])
            n += 1
        st.add(s[i])
        res = max(res, i - n + 1)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring1("abcabcbb"))
print(lengthOfLongestSubstring1("bbbbb"))