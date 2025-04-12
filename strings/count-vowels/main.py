""" 
Write code to count the number of vowels in a string.
"""

def count_vowels1(string):
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
    return count

def count_vowels2(string):
    return sum(1 for char in string if char in 'aeiou')

def count_vowels3(string):
    return len([char for char in string if char in 'aeiou'])

print(count_vowels1('hello'))
print(count_vowels2('hello'))
print(count_vowels3('hello'))