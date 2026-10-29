def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row):
    # Base case: all 8 queens are placed
    if row == 8:
        return True

    # Try each column
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            # Recurse for the next row
            if solve_n_queens_util(board, row + 1):
                return True

            # Backtrack
            board[row][col] = '.'

    return False


# Create 8 x 8 board
board = [['.' for _ in range(8)] for _ in range(8)]

# Solve the problem
if solve_n_queens_util(board, 0):
    print("Solution for 8 Queens Problem:\n")

    for row in board:
        print(' '.join(row))
else:
    print("No solution exists for 8 Queens Problem")