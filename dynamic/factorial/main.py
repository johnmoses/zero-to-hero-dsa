""" 
Factorial by Dynamic Programming
"""

from functools import lru_cache

@lru_cache
def factorial(num: int) -> int:
    """ 
    Return:
    """
    if num < 0:
        raise ValueError("Negative number not acceptable")
        
    return 1 if num in (0, 1) else num * factorial(num-1)

print(factorial(5))