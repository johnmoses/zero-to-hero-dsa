""" 
Search a matrix for a given value
arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]
x = 8
"""
def search1(arr, x):
    if not arr:
        return None
    row = 0
    col = len(arr[0]) - 1
    while row < len(arr) and col >= 0:
        if arr[row][col] == x:
            return (row, col)
        elif arr[row][col] > x:
            col -= 1
        else:
            row += 1
    return None

def search2(arr, x):
    rows, cols = len(arr), len(arr[0])
    # Traverse each row and column
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == x:
                return True
    return False

print(search1([
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
], 8))

print(search2([
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
], 8))
