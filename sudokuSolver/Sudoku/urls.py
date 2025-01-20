from django.urls import path
from django.contrib import admin
from Sudoku import views

urlpatterns = [
    path('', views.index_view, name='index'), 
    path('login/', views.login_view, name='login'),  
    path('level/', views.level_view, name='level'),  
    path('grid/', views.grid_view, name='grid'),  
    path('solver/', views.solver_view, name='solver'), 
    path('solve/', views.solve_sudoku, name='solve_sudoku'),
    path('generate/', views.generate_sudoku, name='generate_sudoku'), 
]