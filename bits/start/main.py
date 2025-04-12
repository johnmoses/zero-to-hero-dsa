"""
Bit manipulation

Write code to demonstrate bit manipulation
"""
def get_bit(num: int, pos: int) -> bool:
    """Get value of bit at given position"""
    return bool(num & (1 << pos))

def set_bit(num: int, pos: int) -> int:
    """Set bit to 1 at given position"""
    return num | (1 << pos)

def clear_bit(num: int, pos: int) -> int:
    """Clear bit at given position"""
    return num & ~(1 << pos)

print(get_bit(5, 1))  # True
print(set_bit(5, 1))  # 7
print(clear_bit(7, 1))  # 5