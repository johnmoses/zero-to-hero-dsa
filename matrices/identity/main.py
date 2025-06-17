""" 
Identity matrix

Create an identify matrix
size = 3
"""
def identityMatrix1(size):
    for row in range(0, size):
        for col in range(0, size):
            if row == col:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

def identityMatrix2(size):
    for row in range(0, size):
        for col in range(0, size):
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()

print(identityMatrix1(3))
print(identityMatrix2(3))