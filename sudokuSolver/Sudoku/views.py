from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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