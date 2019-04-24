from django.shortcuts import render

from .models import ToDo

def todos(request):
	"""Home page of the todos app."""
	### TEST: Please complete
	# Trying to grab all data upfront:
	# Is this ok, or should all be passed in the template? 
	todos = ToDo.objects.all()
	return render(request, 'todo/todos_main.html', {'todos': todos})
	
def todo_details(request, todo_id):
	"""The individual detail page for the ToDo items"""
	# READ PORTION OF APP 
	todo = ToDo.objects.get(id = todo_id)
	return render(request, 'todo/todo_details.html', {'todo': todo})
	
