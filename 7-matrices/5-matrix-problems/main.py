# Matrix Problems - Python Example

def rotate_matrix_90_1(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer -1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # save top
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rotate_matrix_90_1(matrix)
for row in matrix:
    print(row)

def rotate_matrix_90_2(mat):
    if not mat:
        return mat
    mat.reverse()
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

print(rotate_matrix_90_2([[1,2,3],[4,5,6],[7,8,9]]))

def rotate_matrix_90_3(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix_90_3(matrix))