import random

# Step 1: Generate a valid base grid
def generate_base_grid():
    base = list(range(1, 10))
    random.shuffle(base)
    return [[base[(i * 3 + i // 3 + j) % 9] for j in range(9)] for i in range(9)]#base index //cyclic permutation

# Step 2: Shuffle rows and columns within blocks
def shuffle_grid(grid):
    # Shuffle rows within each 3x3 row block
    for i in range(0, 9, 3):
        random.shuffle(grid[i:i+3])

    # Transpose to shuffle columns using the same logic
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    for i in range(0, 9, 3):
        random.shuffle(grid[i:i+3])
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]  # Transpose back

# Step 3: Remove numbers to create the puzzle
def create_puzzle(grid, clues):
    cells = [(r, c) for r in range(9) for c in range(9)]  # All cell positions
    random.shuffle(cells)

    puzzle = [row[:] for row in grid]  # Copy the grid
    for r, c in cells[:81 - clues]:  # Remove numbers to leave only 'clues' filled
        puzzle[r][c] = 0

    # Ensure the puzzle has a unique solution
    if not has_unique_solution(puzzle):
        return create_puzzle(grid, clues)  # Retry if not unique
    return puzzle

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

# Step 4: heristic Backtracking solver to check for unique solution
def has_unique_solution(board):
    """
    Checks if the Sudoku puzzle has a unique solution using a heuristic.
    Returns True if the puzzle has exactly one solution, False otherwise.
    """
    def solve_with_count(board, solutions_found=0):
        row, col, possible_values = find_most_constrained_cell(board)
        if row == -1:  # No empty cells left (a solution is found)
            return solutions_found + 1

        for num in possible_values:
            board[row][col] = num
            solutions_found = solve_with_count(board, solutions_found)
            if solutions_found > 1:  # Stop early if more than one solution
                return solutions_found
            board[row][col] = 0  # Undo placement (backtrack)

        return solutions_found

    # Use a copy of the board to ensure the original is unchanged
    board_copy = [row[:] for row in board]
    return solve_with_count(board_copy) == 1


# Generate and display the puzzle
if __name__ == "__main__":
    base_grid = generate_base_grid()
    shuffled_grid = shuffle_grid(base_grid)
    sudoku_puzzle = create_puzzle(shuffled_grid, clues=36)  # Adjust clues for difficulty

