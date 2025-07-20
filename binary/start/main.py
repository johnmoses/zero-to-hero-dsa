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

def toggle_bit(num, i):
    return num ^ (1 << i)

# Count number of set bits
def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

# Brian Kernighan's algorithm for counting set bits
def count_set_bits_optimized(num):
    count = 0
    while num:
        num &= num - 1  # Removes rightmost set bit
        count += 1
    return count

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_ii(nums):
    ones = twos = 0
    
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    
    return ones

def power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print('Binary Operators: ', binary_operators(2,3))
print('Get Bit: ', get_bit(5, 1))  # True
print('Set Bit: ', set_bit(5, 1))  # 7
print('Clear Bit: ', clear_bit(7, 1))  # 5
print('Toggle Bit: ', toggle_bit(7, 1))  # 5
print('Count Set Bits: ', count_set_bits(7))  # 3
print('Count Set Bits Optimized: ', count_set_bits_optimized(7))  # 3
print('Single Number: ', single_number([1, 2, 3, 1, 3, 2, 4, 4, 5]))
