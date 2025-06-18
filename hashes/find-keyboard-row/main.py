"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
    
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:

Input: words = ["omk"]
Output: []
"""
def find_keyboard_row(words):
    output = []
    for word in words:
        if set(word.lower()) <= set("qwertyuiop"):
            output.append(word)
        elif set(word.lower()) <= set("asdfghjkl"):
            output.append(word)
        elif set(word.lower()) <= set("zxcvbnm"):
            output.append(word)
    return output

print(find_keyboard_row(["Hello","Alaska","Dad","Peace"]))
print(find_keyboard_row(["omk"]))