# Application Examples - Python

# Example: Count frequencies of numbers in ranges efficiently
def count_in_range(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

arr = [1, 2, 2, 3, 3, 3, 4]
max_val = max(arr)
freq = [0] * (max_val + 1)

for num in arr:
    freq[num] += 1

prefix_freq = [0] * len(freq)
prefix_freq = freq
for i in range(1, len(freq)):
    prefix_freq[i] = prefix_freq[i - 1] + freq[i]

print("Count of numbers between 2 and 3:", count_in_range(prefix_freq, 2, 3))
