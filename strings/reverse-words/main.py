"""
Write a function that reverses words in a sentence.

Example:
Input: "Hello world! How are you?"
Output: "you? are How world! Hello"

Note: You can use any built-in or third-party libraries, but you should not use any string manipulation functions.
"""

def reverseWords1(sentence):
    """
    Reverses the order of words in a given sentence.

    Args:
        sentence (str): The input sentence to be reversed.

    Returns:
        str: The sentence with words in reverse order.
    """
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of words
    words.reverse()

    # Join the reversed words back into a sentence
    reversed_sentence = " ".join(words)

    return reversed_sentence

def reverseWords2(s):
    res = s.strip().split()
    n = len(res)
    reverse(res, 0, n - 1)
    return " ".join(res)

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

print(reverseWords1("Hello world! How are you?"))
print(reverseWords2("Hello world! How are you?"))