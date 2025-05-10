""" 
Breadth First Search by queue on a matrix
"""
from collections import deque

def bfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        row, col = queue.popleft()
        
        # Process the current cell (e.g., print its value)
        print(matrix[row][col], end=" ")

        # Explore neighbors (up, down, left, right)
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

start_node = (0, 0) # Top-left corner
bfs(matrix, start_node)