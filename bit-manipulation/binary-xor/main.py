"""
Binary xor bit manipulation
"""
def binary_xor(a: int, b: int) -> str:
    """
    Take 2 integers and convert to binary
    using xor operation
    Return a binary number
    """
    if a < 0 or b < 0:
        raise ValueError("input must be positive integers")
    bin_a = str(bin(a))[2:]
    bin_b = str(bin(b))[2:]

    max_len = max(len(bin_a), len(bin_b))

    return "00" + "".join(
        str(int(char_a != char_b))
        for char_a, char_b in zip(bin_a.zfill(max_len), bin_b.zfill(max_len))
    )

print(binary_xor(10, 5)) 