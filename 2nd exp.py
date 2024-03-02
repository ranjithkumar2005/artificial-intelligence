def safe(board, row, col):
    # Check if there is a queen in the same row
    if any(board[row]):
        return False

    # Check if there is a queen in the same column
    if any(board[i][col] for i in range(len(board))):
        return False

    # Check if there is a queen in the same diagonal (upper left to lower right)
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check if there is a queen in the same diagonal (upper right to lower left)
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, len(board)))):
        return False

    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def solve_queens(board, row):
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if safe(board, row, col):
            board[row][col] = 1
            solve_queens(board, row + 1)
            board[row][col] = 0  # Backtrack

if __name__ == "__main__":
    board_size = 8
    chessboard = [[0] * board_size for _ in range(board_size)]

    solve_queens(chessboard, 0)
