# Dynamic Programming Intro - Python example
# Compute Fibonacci numbers using memoization

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} is {fib(n)}")
