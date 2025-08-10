""" 
A basic matrix data structure implementation
"""
from collections import deque

class Matrix:
    def __init__(self, rows, cols):
        """
        Initialize matrix with given dimensions
        Args:
            rows: Number of rows
            cols: Number of columns
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    @classmethod
    def from_list(cls, data):
        """
        Create matrix from 2D list
        Args:
            data: 2D list of values
        """
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0
        matrix = cls(rows, cols)
        matrix.matrix = [row[:] for row in data]
        return matrix

    def get(self, row, col):
        """Get element at specified position"""
        if self._is_valid_position(row, col):
            return self.matrix[row][col]
        raise IndexError("Matrix index out of range")
    
    def set(self, row, col, value):
        """Set element at specified position"""
        if self._is_valid_position(row, col):
            self.matrix[row][col] = value
        else:
            raise IndexError("Matrix index out of range")
    
    def add(self, other):
        """Add another matrix to this one"""
        if not self._is_same_size(other):
            raise ValueError("Matrices must have same dimensions")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result
    
    def subtract(self, other):
        """Subtract another matrix from this one"""
        if not self._is_same_size(other):
            raise ValueError("Matrices must have same dimensions")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result
    
    def multiply(self, other):
        """Multiply with another matrix"""
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal rows in second")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result
    
    def scalar_multiply(self, scalar):
        """Multiply matrix by a scalar"""
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] * scalar
        return result
    
    def transpose(self):
        """Return transpose of the matrix"""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result
    
    def is_square(self):
        """Check if matrix is square"""
        return self.rows == self.cols
    
    def get_row(self, row):
        """Get a specific row"""
        if 0 <= row < self.rows:
            return self.matrix[row][:]
        raise IndexError("Row index out of range")
    
    def get_col(self, col):
        """Get a specific column"""
        if 0 <= col < self.cols:
            return [self.matrix[i][col] for i in range(self.rows)]
        raise IndexError("Column index out of range")
    
    def _is_valid_position(self, row, col):
        """Check if position is valid"""
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def _is_same_size(self, other):
        """Check if two matrices have same dimensions"""
        return self.rows == other.rows and self.cols == other.cols
    
    def __str__(self):
        """String representation of matrix"""
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    def __repr__(self):
        """Detailed string representation of matrix"""
        return f"Matrix({self.rows}x{self.cols}):\n{self.__str__()}"

    def get_neighbors(self, node):
        """Get neighbors of a node"""
        return self.matrix.get(node, [])

    def dfs(self, start, target):
        """Depth First Search"""
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node == target:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(self.get_neighbors(node))
        return False

    def bfs(self, start, target):
        """Breadth First Search"""
        visited = set()
        queue = deque([start, [start]])
        while queue:
            node, path = queue.popleft()
            if node == target:
                return True, path
            if node not in visited:
                visited.add(node)
                for neighbor in self.get_neighbors(node):
                    queue.append((neighbor, path + [neighbor]))
        return False, []


# Create matrix with rows and columns
m1 = Matrix(3, 3)
m1.set(0, 0, 1)
m1.set(1, 1, 2)
m1.set(2, 2, 3)

# Create from lists
m2 = Matrix.from_list([[1, 2, 3],[4, 5, 6]])
m3 = Matrix.from_list([[7, 8, 9],[10, 11, 12]])

print("\nM1:")
print(m1)
print("\nM2:")
print(m2)
print("\nM3:")
print(m3)
       
# Test addition
print("\nAddition:")
print(m2.add(m3))

# Test subtraction
print("\nSubtraction:")
print(m2.subtract(m3))

# Test scalar multiplication
print("\nScalar multiplication (m1 * 2):")
print(m2.scalar_multiply(2))
    

# Test DFS
# print("\nDFS path to find value 7 from (0,0):")
# path = m3.dfs((0, 0), 7)
# print(f"Path: {path}")

# Test BFS
# print("\nBFS shortest path to find value 7 from (0,0):")
# path = m3.bfs((0, 0), 7)
# print(f"Path: {path}")