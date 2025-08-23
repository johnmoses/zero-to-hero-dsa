"""
main.py

Examples demonstrating Big-O time complexity in Python.
"""

def constant_time_example(arr):
    # O(1) - Accessing first element
    return arr[0]

def linear_time_example(arr):
    # O(n) - Loop through all elements
    for item in arr:
        print(item)

def quadratic_time_example(arr):
    # O(n^2) - Nested loops
    for i in arr:
        for j in arr:
            print(i, j)

if __name__ == "__main__":
    sample = [1, 2, 3, 4]
    
    print("Constant time example:")
    print(constant_time_example(sample))
    
    print("\nLinear time example:")
    linear_time_example(sample)
    
    print("\nQuadratic time example:")
    quadratic_time_example(sample)
