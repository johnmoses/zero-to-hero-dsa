"""
Search sorted two-dimensional matrix given dimensions m, n and target key k.

mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
"""
def searchSorted1(mat, m, n, k):
    # Perform binary search on 2D matrix
    if not mat or not mat[0]:
        return False
        
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        
        if mat[row][col] == k:
            return True
        elif mat[row][col] < k:
            left = mid + 1 
        else:
            right = mid - 1
    return False

def searchSorted2(mat: list[list], m: int, n: int, key: int | float) -> None:
    """
    Search a sorted matrix
    """
    i, j = m-1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            print(f"key {key} found at row- {i+1} column- {j+1}")
            return
        if key < mat[i][j]:
             i -= 1
        else:
            j += 1
    print(f"key {key} not found")

print(searchSorted1([[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 2, 2, 2))
print(searchSorted2([[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 2, 2, 2))