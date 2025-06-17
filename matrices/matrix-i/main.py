""" 
Write a basic matrix data structure
"""
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = [[0] * cols for _ in range(rows)]

    def get(self, row, col):
        return self.values[row][col]

    def set(self, row, col, value):
        self.values[row][col] = value

    def display(self):
        for row in self.values:
            print(row)

class Matrix1:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = [[0] * cols for _ in range(rows)]

    def get(self, row, col):
        return self.values[row][col]

    def set(self, row, col, value):
        self.values[row][col] = value

    def display(self):
        for row in self.values:
            print(row)

matrix = Matrix1(3, 3)
matrix.set(0, 0, 1)
matrix.set(1, 1, 2)
matrix.set(2, 2, 3)
print(matrix.get(0, 0))  # Output: 1
print(matrix.get(1, 1))  # Output: 2
print(matrix.get(2, 2))  # Output: 3
print(matrix.display())  # Output: [1, 0, 0], [0, 2, 0], [0, 0, 3]

