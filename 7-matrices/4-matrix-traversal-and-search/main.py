# Matrix Traversal and Search - Python Example

def search_in_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix)
    r, c = 0, cols - 1
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return (r, c)
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return (-1, -1)

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10,13,14,17]
]

print("Target 5 at:", search_in_matrix(matrix, 5))
