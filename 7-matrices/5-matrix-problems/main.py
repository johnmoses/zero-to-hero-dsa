# Matrix Problems - Python Example

def rotate_matrix_90(matrix):
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

rotate_matrix_90(matrix)
for row in matrix:
    print(row)
