# todo\urls.py
# 04.24.19

from django.urls import path 

from . import views

urlpatterns = [
	path('', views.todos, name = 'todos_main'),
	path('<int:todo_id>/', views.todo_details, name = 'todo_details'),
]

# NOTE: 
# DO NOT put a space between int: and the variable. 
