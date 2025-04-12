"""
Write dynamic programing algorithm for nth fibonacci number

"""
def nthFiboacci1(n):
    if n==0: 
        return 0
    if n==1: 
        return 1
    return nthFiboacci1(n-1) + nthFiboacci1(n-2)

def nthFiboacci2(n):
    if n==0: 
        return 0
    if n==1: 
        return 1

    F = [None] * (n + 1)
    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]

print(nthFiboacci1(10))
print(nthFiboacci2(10))
