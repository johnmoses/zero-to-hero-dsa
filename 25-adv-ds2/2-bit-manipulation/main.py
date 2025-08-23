# Advanced Data Structures 2 - Intro Python example
# Bit manipulation example: Counting set bits in an integer

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove the lowest set bit
        count += 1
    return count

if __name__ == "__main__":
    num = 29  # Binary: 11101
    print(count_set_bits(num))  # Output: 4
