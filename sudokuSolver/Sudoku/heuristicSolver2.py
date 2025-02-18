import time

def solve_normal(board):
    start_time = time.time()
    # Rest of your existing solve_with_optimized_heuristic code stays the same
    result = solve_with_optimized_heuristic(board)  # Rename your current function to this
    end_time = time.time()
    solve_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, solve_time

def get_affected_cells(row, col):
    """Returns set of cells that would be affected by placing a number at (row, col)"""
    affected = set()
    
    # Add all cells in same row
    for c in range(9):
        if c != col:
            affected.add((row, c))
    
    # Add all cells in same column
    for r in range(9):
        if r != row:
            affected.add((r, col))
    
    # Add all cells in same 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if (r, c) != (row, col):
                affected.add((r, c))
                
    return affected

def initialize_possibilities(board):
    """Create initial dictionary of possibilities for all empty cells"""
    possibilities = {}
    
    # First set all empty cells to have all possibilities
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possibilities[(row, col)] = set(range(1, 10))
    
    # Then remove possibilities based on existing numbers
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                value = board[row][col]
                # Remove this value from all affected cells
                for r, c in get_affected_cells(row, col):
                    if (r, c) in possibilities:
                        possibilities[(r, c)].discard(value)
    
    return possibilities

def find_most_constrained_cell(possibilities):
    """Find the empty cell with fewest possible values"""
    if not possibilities:  # If no empty cells left
        return -1, -1, []
        
    # Find cell with minimum number of possibilities
    min_possibilities = 10
    best_cell = (-1, -1)
    best_values = []
    
    for (row, col), possible_values in possibilities.items():
        if len(possible_values) < min_possibilities:
            min_possibilities = len(possible_values)
            best_cell = (row, col)
            best_values = possible_values
            
    return best_cell[0], best_cell[1], list(best_values)

def solve_with_optimized_heuristic(board):
    """Solves Sudoku using optimized heuristic approach with dynamic possibility tracking"""
    # Initialize possibilities for all empty cells
    possibilities = initialize_possibilities(board)
    
    # Find most constrained cell
    row, col, possible_values = find_most_constrained_cell(possibilities)
    
    # If no empty cells are left, puzzle is solved
    if row == -1:
        return True
        
    # If any cell has no possibilities, this branch is invalid
    if not possible_values:
        return False
    
    # Save current possibilities for backtracking
    saved_possibilities = {k: v.copy() for k, v in possibilities.items()}
    
    # Try each possible value
    for value in possible_values:
        # Place the value
        board[row][col] = value
        
        # Remove this cell from possibilities
        del possibilities[(row, col)]
        
        # Update possibilities for affected cells
        for affected_row, affected_col in get_affected_cells(row, col):
            if (affected_row, affected_col) in possibilities:
                possibilities[(affected_row, affected_col)].discard(value)
        
        # Recursive call
        if solve_with_optimized_heuristic(board):
            return True
            
        # Backtrack: restore board and possibilities
        board[row][col] = 0
        possibilities.clear()
        possibilities.update(saved_possibilities)
    
    return False