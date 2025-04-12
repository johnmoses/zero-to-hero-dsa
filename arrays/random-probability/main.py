""" 
Generate several, say 10 random probability arrays where each sums up to 1 and whose mean is [0.5, 0.5, 0] 
"""

import random

for i in range(10):
    arr = [random.random() for _ in range(3)]
    total = sum(arr)
    arr = [x / total for x in arr]
    print(arr)

    mean = sum(arr) / len(arr)
    print(mean)
    print()

    if mean != 0.5:
        print("Mean is not 0.5")
        break
else:
    print("All means are 0.5")