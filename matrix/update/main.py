""" 
Update matrix
"""

from typing import List

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell:
                    top = mat[i-1][j] if i else float('inf')
                    left = mat[i][j-1] if j else float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := mat[i][j]:
                    bottom = mat[i+1][j] if i < m - 1 else float('inf')
                    right = mat[i][j+1] if j < n - 1 else float('inf')
                    mat[i][j] = min(cell, bottom + 1, right + 1)
        return mat
    

mat = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(mat))