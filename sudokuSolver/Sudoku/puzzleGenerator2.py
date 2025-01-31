import random
import copy

def is_valid_move(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    
    row, col = empty
    for num in random.sample(range(1, 10), 9):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku(clues):
    # Create empty grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    
    # Generate a solved sudoku by filling diagonals and solving
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                grid[i + j][i + k] = nums.pop()
    
    # Solve the grid
    solve_sudoku(grid)
    
    # Create a deep copy of the solved grid
    solution = [row[:] for row in grid]
    
    # Remove numbers to create puzzle
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    
    # Calculate how many cells to empty
    cells_to_empty = 81 - clues
    
    # Remove numbers
    for i in range(cells_to_empty):
        if i < len(cells):
            row, col = cells[i]
            grid[row][col] = 0
    
    return grid, solution