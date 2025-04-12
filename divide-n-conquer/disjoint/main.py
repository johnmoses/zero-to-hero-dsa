"""
Calculating disjointness of a set

Input Data:
    setA = [1,3,5,7,9]
    setB = [2,4,6,8,10]
    setC = [0,1,13]
"""

def disjoint(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

print(disjoint([1,3,5,7,9], [2,4,6,8,10], [0,1,13]))