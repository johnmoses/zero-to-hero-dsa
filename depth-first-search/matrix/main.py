""" 
Depth First Search on a matrix

Given a 2d matrix, perform DFS on it

Example 1:

Input: matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output: 1 2 3 4 8 12 11 10 9 5 6 7
"""
def dfs_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    result = []
    
    def dfs(row, col):
        # Check boundaries and if visited
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            (row,col) in visited):
            return
            
        visited.add((row,col))
        result.append(matrix[row][col])
        
        # DFS in all 4 directions
        for nr, nc in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
            dfs(nr, nc)
            
    dfs(0, 0)
    return result

print(dfs_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

# Output: 1, 4, 7, 8, 5, 2, 3, 6, 9
