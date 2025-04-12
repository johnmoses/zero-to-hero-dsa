""" 
Design a tic-tac-toe game
"""
class TicTacToe:
    def __init__(self, n):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row, col, player):
        if self.board[row][col] == 0:
            self.board[row][col] = player
            return self.check_win(row, col, player)
        return False

    def check_win(self, row, col, player):
        # check row
        if all(self.board[row][c] == player for c in range(self.n)):
            return True
        # check col
        if all(self.board[r][col] == player for r in range(self.n)):
            return True
        # check diag
        if row == col and all(self.board[i][i] == player for i in range(self.n)):
            return True
        # check anti-diag
        if row + col == self.n - 1 and all(self.board[i][self.n - 1 - i] == player for i in range(self.n)):
            return True
        return False

game = TicTacToe(3)
print(game.move(0, 0, 1))  # Player 1 makes a move at (0, 0)
print(game.move(0, 1, 2))  # Player 2 makes a move at (0, 1)
print(game.move(0, 2, 1))  # Player 1 makes a move at (0, 2)
print(game.move(1, 1, 2))  # Player 2 makes a move at (1, 1)
print(game.move(2, 2, 1))  # Player 1 makes a move at (2, 2)
print(game.move(2, 0, 2))  # Player 2 makes a move at (2, 0)
print(game.move(1, 0, 1))  # Player 1 makes a move at (1, 0)
print(game.move(2, 1, 2))  # Player 2 makes a move at (2, 1)
print(game.move(1, 2, 1))  # Player 1 makes a move at (1, 2)
print(game.move(2, 2, 2))  # Player 2 makes a move at (2, 2)