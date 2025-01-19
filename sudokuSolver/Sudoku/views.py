from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .heuristicSolver import solve_with_heuristic
from .puzzleGenerator import generate_base_grid, shuffle_grid, create_puzzle

# Create your views here.

@csrf_exempt
def generate_sudoku(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            clues = body.get('clues', 36)  # Default to 36 clues if not provided
            base_grid = generate_base_grid()
            shuffled_grid = shuffle_grid(base_grid)
            sudoku_puzzle = create_puzzle(shuffled_grid, clues)
            return JsonResponse({'puzzle': sudoku_puzzle})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def index_view(request):
    return render(request, 'Sudoku\index.html')

def level_view(request):
    return render(request, 'Sudoku\level.html')

def grid_view(request):
    return render(request, 'Sudoku\grid.html')

def login_view(request):
    return render(request, 'Sudoku\login.html')

def solver_view(request):
    return render(request, 'Sudoku\solver.html')