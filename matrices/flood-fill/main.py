""" 
Perform flood fill on a 2D grid. Change all the cells connected to the starting cell to new color.

Example:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
"""
def floodFill(image, sr, sc, newColor):
    if not image or image[sr][sc] == newColor:
        return image
        
    oldColor = image[sr][sc]
    rows = len(image)
    cols = len(image[0])
    dfs(image, sr, sc, oldColor, newColor, rows, cols)
    return image

def dfs(image, r, c, oldColor, newColor, rows, cols):
    if (r < 0 or r >= rows or c < 0 or c >= cols or 
        image[r][c] != oldColor):
        return
        
    image[r][c] = newColor
    dfs(image, r+1, c, oldColor, newColor, rows, cols)
    dfs(image, r-1, c, oldColor, newColor, rows, cols) 
    dfs(image, r, c+1, oldColor, newColor, rows, cols)
    dfs(image, r, c-1, oldColor, newColor, rows, cols)

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))