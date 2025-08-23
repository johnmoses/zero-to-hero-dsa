# Big O Basics - Python Example

def constant_time(items):
    return items[0]  # O(1)

def linear_time(items):
    for item in items:
        print(item)  # O(n)
    return len(items)

def logarithmic_time(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count  # O(log n)

def quadratic_time(items):
    count = 0
    for i in items:
        for j in items:
            count += 1
    return count  # O(n^2)

def exponential_time(n):
    if n <= 1:
        return 1
    return exponential_time(n-1) + exponential_time(n-1)  # O(2^n)

def polynomial_time(n, k):
    count = 0
    for i in range(n**k):
        count += 1
    return count  # O(n^k)

def factorial_time(n):
    if n <= 1:
        return 1
    return n * factorial_time(n-1)  # O(n!)

print("Constant time result:", constant_time([1,2,3]))
print("Logarithmic steps:", logarithmic_time(16))
print("Quadratic operations:", quadratic_time([1,2,3]))
