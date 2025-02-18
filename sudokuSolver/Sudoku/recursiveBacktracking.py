import time 

def solve_normal(board):
    start_time = time.time()
    # Rest of your existing solve_normal code stays the same
    result = solve_backtracking(board)  # Rename your current function to this
    end_time = time.time()
    solve_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, solve_time
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_backtracking(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_normal(board):
                            return True
                        board[row][col] = 0
                return False
    return True