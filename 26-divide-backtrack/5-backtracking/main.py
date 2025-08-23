# Backtracking - Python example (N-Queens)

def solve_n_queens(n):
    def is_not_under_attack(row, col):
        return not (cols[col] or hills[row - col] or dales[row + col])

    def place_queen(row, col):
        queens.add((row, col))
        cols[col] = 1
        hills[row - col] = 1
        dales[row + col] = 1

    def remove_queen(row, col):
        queens.remove((row, col))
        cols[col] = 0
        hills[row - col] = 0
        dales[row + col] = 0

    def backtrack(row=0):
        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    solutions.append(list(queens))
                else:
                    backtrack(row + 1)
                remove_queen(row, col)

    cols = [0] * n
    hills = [0] * (2 * n - 1)  # "hill" diagonals
    dales =  [0] * (2 * n - 1)  # "dale" diagonals
    queens = set()
    solutions = []
    backtrack()
    return solutions

if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-Queens:", len(solutions))
