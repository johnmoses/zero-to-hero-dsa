# Matrix Operations - Python Example

def add_matrices(A, B):
    n, m = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def transpose_matrix(A):
    n, m = len(A), len(A)
    return [[A[j][i] for j in range(n)] for i in range(m)]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Added matrix:")
for row in add_matrices(A, B):
    print(row)

print("Transposed matrix:")
for row in transpose_matrix(A):
    print(row)
