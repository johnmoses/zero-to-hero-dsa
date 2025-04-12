"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard.

For example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

words = ["Hello", "Alaska", "Dad", "Peace"]

def find_keyboard_row(words):
    keyboard = [
        set('quertyuiop'),
        set('asdfghjkl'),
        set('zxcvbnm'),
    ]
    res = []
    for word in words:
        for key in keyboard:
            if set(word.lower()).issubset(key):
                res.append(word)
    return res

print(find_keyboard_row(words))