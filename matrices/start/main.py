"""
Matrix and Operations

Basic operations of a matrix
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Matrix: ', matrix)

# Transpose or inverse
transpose = [[row[i] for row in matrix] for i in range(3)]
print('Transpose: ', transpose)

# Multiplication
multiplication = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in matrix]
print('Multiplication: ', multiplication)

# Determinant
determinant = sum(a * b * c for a, b, c in zip(matrix[0], matrix[1], matrix[2]))
print('Determinant: ', determinant)

# Trace
trace = sum(matrix[i][i] for i in range(3))
print('Trace: ', trace)

# Eigenvalues and Eigenvectors
eigenvalues = [sum(matrix[i][j] for i in range(3)) for j in range(3)]
print('Eigenvalues: ', eigenvalues)

eigenvectors = [[row[i] for row in matrix] for i in range(3)]
print('Eigenvectors: ', eigenvectors)

# Rank
rank = len(set(tuple(row) for row in matrix))
print('Rank: ', rank)

# Singular Value Decomposition
u, s, vh = matrix
print('U: ', u)
print('S: ', s)
print('Vh: ', vh)

# Condition Number
condition_number = max(s) / min(s)
print('Conditional number: ', condition_number)

# Cholesky Decomposition
cholesky = matrix
print('Cholesky: ', cholesky)

# Accessing elements of 2-D array
print("Row 1 column 1:", matrix[0][0])
print("Row 2 column 2:", matrix[1][1])
print("Row 3 column 3:", matrix[2][2])

# Traversing each row
print('Traversing')
# Loop through each row
for row in matrix:
    # Traversing each element in the current row
    for col in row:
        print(col, end=" ")
    print()
    
# Creating a 2d matrix with initial values, say zeroes
rows, cols = (3, 3)
mat2d = [[0] * cols] * rows
print('2D 1: ', mat2d)

# Alternative
mat2d = [[0] * cols for _ in range(rows)]   # _ may be i, r or whatever
print('2D 2: ', mat2d)

# Updating the matrix
mat2d[1][2] = 3
print('2D updated', mat2d)