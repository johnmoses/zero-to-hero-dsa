""" 
Find the longest word in a sentence.
"""

def longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The longest word in the sentence.
    """
    # Split the sentence into a list of words
    words = sentence.split()

    # Initialize the longest word with the first word in the list
    longest = words[0]

    # Iterate through the list of words
    for word in words:
        # If the current word is longer than the current longest word
        if len(word) > len(longest):
            # Update the longest word
            longest = word

    # Return the longest word
    return longest
    
print(longest_word("The quick brown fox jumps over the lazy dog"))