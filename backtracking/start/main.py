"""
Back tracking

Write a simple backtrack algorithm for n-queens problem
"""
def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n):
    if row == n:
        for r in board:
            print(r)
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n)
            board[row][col] = 0  # Backtrack

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens_util(board, 0, n)

solve_nqueens(4)
