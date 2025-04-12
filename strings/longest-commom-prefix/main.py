"""
String algorithms

Find the longest common prefix

Example 1:
    
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
    
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
    
All given inputs are in lowercase letters a-z.
"""
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    current = strs[0]
    for i in range(1, len(strs)):
        temp = ""
        if len(current) == 0:
            break
        for j in range(len(strs[i])):
            if j < len(current) and current[j] == strs[i][j]:
                temp += current[j]
            else:
                break
        current = temp
    return current

print(longestCommonPrefix(["flower","flow","flight"]))