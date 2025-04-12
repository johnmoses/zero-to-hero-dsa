"""  
Draw histogram of count of friends
"""

from collections import Counter
from matplotlib import pyplot as plt
import random

def draw_histogram():
    # Generate data
    num_friends = [random.randint(1, 120) for _ in range(1025)]
    counts = Counter(num_friends)
    xs = range(101)
    ys = [counts[x] for x in xs]

    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Counts Histogram")
    plt.show()

def main():
    draw_histogram()

if __name__ == "__main__":
    main()