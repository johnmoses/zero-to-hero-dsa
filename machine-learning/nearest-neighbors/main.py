""" 
Nearest neighbor algorithm
"""

import math

def distance(x, y):
    assert len(x) == len(y), "The vector must have same length"
    result = ()
    sum = 0
    for i in range(len(x)):
        result += (x[i] -y[i],)
    for component in result:
        sum += component**2
    return math.sqrt(sum)

def nearest_neighbor(x, tset):
    assert isinstance(x, tuple) and isinstance(tset, dict)
    current_key = ()
    min_d = float('inf')
    for key in tset:
        d = distance(x, key)
        if d < min_d:
            min_d = d
            current_key = key
    return tset[current_key]