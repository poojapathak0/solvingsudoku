/*// Get all cell elements
const cells = document.querySelectorAll('.sudoku-grid .cell');
const solveButton = document.querySelector('#solve');
const numberButtons = document.querySelectorAll('.boxes .cell');

// Initialize selected cell tracking
let selectedCell = null;

// Add click handlers to grid cells
cells.forEach((cell, index) => {
    cell.addEventListener('click', () => {
        // Remove previous selection
        if (selectedCell) {
            selectedCell.classList.remove('selected');
        }
        cell.classList.add('selected');
        selectedCell = cell;
    });
});

// Add click handlers to number buttons
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (selectedCell) {
            selectedCell.textContent = button.textContent;
        }
    });
});

// Function to get current grid state
function getGridState() {
    const grid = [];
    let currentRow = [];
    
    cells.forEach((cell, index) => {
        const value = cell.textContent.trim() === '' ? 0 : parseInt(cell.textContent);
        currentRow.push(value);
        
        if (currentRow.length === 9) {
            grid.push(currentRow);
            currentRow = [];
        }
    });
    
    return grid;
}

// Function to update grid with solution
function updateGrid(solution) {
    solution.forEach((row, rowIndex) => {
        row.forEach((value, colIndex) => {
            const cellIndex = rowIndex * 9 + colIndex;
            cells[cellIndex].textContent = value;
        });
    });
}

// Add click handler to solve button
solveButton.addEventListener('click', async () => {
    const grid = getGridState();
    
    try {
        const response = await fetch('/solve_sudoku/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ grid: grid })
        });
        
        const data = await response.json();
        
        if (data.success) {
            updateGrid(data.solution);
        } else {
            alert('Unable to solve the puzzle: ' + data.error);
        }
    } catch (error) {
        alert('Error solving puzzle: ' + error.message);
    }
});

// Optional: Add keyboard input support
document.addEventListener('keydown', (event) => {
    if (!selectedCell) return;
    
    if (event.key >= '1' && event.key <= '9') {
        selectedCell.textContent = event.key;
    } else if (event.key === 'Backspace' || event.key === 'Delete') {
        selectedCell.textContent = '';
    }
});

cells.forEach(input => {
    input.addEventListener('input', function() {
        this.classList.add('new-number');
        setTimeout(() => {
            this.classList.remove('new-number');
        }, 200);
    });
});*/