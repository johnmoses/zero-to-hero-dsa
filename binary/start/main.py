"""
Bit manipulation

Write code to demonstrate bit manipulation
"""

def binary_operators(a, b):
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT": ~a,  # ~a = -a-1 in python
        "Left Shift (a << b)": a << b,  # left shift 'a' by 'b' bits
        "Right Shift (a >> b)": a >> b,  # right shift 'a' by 'b' bits
        "Mask": a & 1,  # gives you the least significant bit of a
    }


def get_bit(num: int, pos: int) -> bool:
    """Get value of bit at given position"""
    return bool(num & (1 << pos))


def set_bit(num: int, pos: int) -> int:
    """Set bit to 1 at given position"""
    return num | (1 << pos)


def clear_bit(num: int, pos: int) -> int:
    """Clear bit at given position"""
    return num & ~(1 << pos)

print(binary_operators(2,3))
print(get_bit(5, 1))  # True
print(set_bit(5, 1))  # 7
print(clear_bit(7, 1))  # 5
