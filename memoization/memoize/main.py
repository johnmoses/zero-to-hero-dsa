"""
Memoization
"""

def F(n):
    if memo[n] is not None:  # Already computed
        return memo[n]
    else:  # Computation needed
        print('Computing F(' + str(n) + ')')
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = F(n - 1) + F(n - 2)
        return memo[n]

memo = [None]*7
print('F(6) = ',F(6))
print('memo = ',memo)