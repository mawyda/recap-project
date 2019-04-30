# todo\urls.py
# 04.24.19

from django.urls import path 

from . import views

urlpatterns = [
	path('', views.todos, name = 'todos_main'),
	path('<int:todo_id>/', views.todo_details, name = 'todo_details'),
	path('edit_todo/<int:todo_id>/', views.todo_edit, 
		name = 'todo_edit'),
	path('create_todo/', views.todo_create, name = 'create_todo'),
]

# NOTE: 
# DO NOT put a space between int: and the variable. 
