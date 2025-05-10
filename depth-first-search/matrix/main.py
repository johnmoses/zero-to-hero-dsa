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
    
    def dfs(r, c):
        # Check boundaries and if visited
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r,c) in visited):
            return
            
        visited.add((r,c))
        result.append(matrix[r][c])
        
        # DFS in all 4 directions
        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            dfs(nr, nc)
            
    dfs(0, 0)
    return result

print(dfs_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
