""" 
Data compression

Write a basic data compression algorithm
"""

def compress(data):
    """
    Compresses a string by replacing consecutive repeating characters with the character and the number of times it repeats.

    Args:
        data: The string to compress.

    Returns:
        The compressed string.
    """
    if not data:
        return ""

    compressed = ""
    count = 1
    for i in range(len(data)):
        if i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
        else:
            compressed += data[i] + str(count)
            count = 1
    return compressed


def decompress(data):
    """
    Decompresses a string compressed by the compress function.

    Args:
        data: The compressed string.

    Returns:
        The decompressed string.
    """
    if not data:
        return ""

    decompressed = ""
    i = 0
    while i < len(data):
        char = data[i]
        j = i + 1
        num_str = ""
        while j < len(data) and data[j].isdigit():
            num_str += data[j]
            j += 1
        num = int(num_str)
        decompressed += char * num
        i = j
    return decompressed


data = "aaabbbcccdddeee"
compressed_data = compress(data)
print(f"Compressed data: {compressed_data}")
decompressed_data = decompress(compressed_data)
print(f"Decompressed data: {decompressed_data}")

data = "aabbccddeeff"
compressed_data = compress(data)
print(f"Compressed data: {compressed_data}")
decompressed_data = decompress(compressed_data)
print(f"Decompressed data: {decompressed_data}")

