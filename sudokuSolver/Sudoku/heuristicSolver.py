import time

def find_most_constrained_cell(board):
    """
    Finds the most constrained cell on the board (the cell with the fewest valid options).
    Returns the cell's coordinates and its possible values.
    """
    min_possibilities = 10  # Start with a number greater than max possibilities (1-9)
    best_cell = (-1, -1)  # Default value for no valid cells
    best_possible_values = []  # Stores the possible values for the most constrained cell

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # If the cell is empty
                possible_values = [
                    num for num in range(1, 10) if is_valid(board, row, col, num)
                ]
                if len(possible_values) < min_possibilities:
                    min_possibilities = len(possible_values)
                    best_cell = (row, col)
                    best_possible_values = possible_values

    return best_cell[0], best_cell[1], best_possible_values #since tuples are ordered best_cell = (row,coumn)


def is_valid(board, row, col, num):
    """
    Checks if placing `num` in cell `(row, col)` is valid according to Sudoku rules.
    """
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def ai_solve_with_heuristic(board):
    """
    Solves the Sudoku puzzle using backtracking and a heuristic to select the most constrained cell.
    """
    row, col, possible_values = find_most_constrained_cell(board)
    if row == -1:  # If no empty cells are left, the board is solved
        return True

    # Try all valid numbers for the selected cell
    for num in possible_values:
        board[row][col] = num
        if ai_solve_with_heuristic(board):  # Recursive call
            return True
        board[row][col] = 0  # Undo placement (backtrack)

    return False  # Trigger backtracking


def print_board(board):
    """
    Prints the Sudoku board in a readable format.
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


# Example Sudoku Puzzle
def generate_sudoku():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

# Generate test puzzles
board = generate_sudoku()

print("Original Puzzle:")
print_board(board)




def benchmark_solver(solver, puzzle, label):
    # Create a deep copy of the puzzle to avoid modifying the original
    import copy
    puzzle_copy = copy.deepcopy(puzzle)
    
    start_time = time.time()
    solver(puzzle_copy)  # Solve the puzzle
    elapsed_time = time.time() - start_time

    elapsed_time_ms = elapsed_time * 1000
    print(f"{label} solved in {elapsed_time_ms:.2f} milliseconds")



# Benchmark both solvers
benchmark_solver(ai_solve_with_heuristic, board, "optimized Backtracking")

ai_solve_with_heuristic(board)

print("\nSolved Sudoku with Heuristic:")
print_board(board)

