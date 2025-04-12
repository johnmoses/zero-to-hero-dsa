""" 
Introduction

Write a generator s_generator(alphabet, length, start_s, end_s) that generates strings of length n over a given alphabet in dictionary order starting with start_s and ending at end_s.

For example, s_generator('ab', 4, 'aaaa', 'bbbb') generates ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']. And s_generator('ab', 4, 'abaa', 'abaa') generates ['abaa', 'abab', 'abba', 'abbb', 'baaa']
"""
def s_generator(alphabet, length, start_s, end_s):
    # Iterate over the range of possible strings from start_s to end_s
    # Get the first character of the range
    for i in range(ord(start_s[0]), ord(end_s[0]) + 1):
        # Get the second character of the range
        for j in range(ord(start_s[1]), ord(end_s[1]) + 1):
            # Get back the first and second characters to to produce the string
            yield chr(i) + chr(j)

print(list(s_generator('ab', 4, 'aaaa', 'bbbb')))
print(list(s_generator('ab', 4, 'abaa', 'abaa')))