"""
You are given an n x n 2D mat representing an image.

Rotate the image by 90 degrees (clockwise).

mat = [[1,2,3],[4,5,6],[7,8,9]]

Follow up:
Could you do this in-place?
"""

def rotate(mat):
    if not mat:
        return mat
    mat.reverse()
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
