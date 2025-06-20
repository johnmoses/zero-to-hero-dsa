""" 
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
def isValid(s: str) -> bool:
    """
    Check if string of parentheses is valid
    """
    # Map closing brackets to opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Stack to track opening brackets
    stack = []
    
    # Check each character in string
    for char in s:
        # If closing bracket found
        if char in brackets:
            # Stack is empty or brackets don't match
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    # If stack is empty, all brackets were closed
    return not stack

def isValid1(s: str) -> bool:
    # Map closing brackets to corresponding open brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Stack to track open brackets
    stack = []
    
    for char in s:
        # If closing bracket
        if char in brackets:
            # Check if matches top of stack
            if not stack or stack.pop() != brackets[char]:
                return False
        # If opening bracket    
        else:
            stack.append(char)
            
    # Check if any unclosed brackets
    return len(stack) == 0

def isValid2(s: str) -> bool:
    brackets = {')':'(','}':'{',']':'['}
    stack = []
    for char in s:
        if char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid1("()"))  # True
print(isValid1("()[]{}"))  # True
print(isValid1("(]"))  # False
print(isValid2("()[]{}"))  # True
print(isValid2("(]"))  # False