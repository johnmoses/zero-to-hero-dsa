# Matrix Basics - Python Example

def identity_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

mat = identity_matrix(3)
for row in mat:
    print(row)
