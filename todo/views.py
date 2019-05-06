# todo\views.py 
# 04.30.2019


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 

from .models import ToDo
from .forms import ToDoForm

def todos(request):
	"""Home page of the todos app."""
	### TEST: Please complete
	# Trying to grab all data upfront:
	# Is this ok, or should all be passed in the template? 
	todos = ToDo.objects.all()
	return render(request, 'todo/todos_main.html', {'todos': todos})
	
def todo_details(request, todo_id):
	"""The individual detail page for the ToDo items"""
	# the "read" portion of crud
	todo = ToDo.objects.get(id = todo_id)
	return render(request, 'todo/todo_details.html', {'todo': todo})
	
def todo_edit(request, todo_id):
	""" View for editing ta ToDo entry."""
	# Get the object from DB 
	todo = ToDo.objects.get(id = todo_id)
	# Fill the form with the data, then send to the below render 
	if request.method != 'POST':
		# Fill the form with the data needed. 
		form = ToDoForm(instance = todo)
	else:
		# Posting data. create instance with data post.
		form = ToDoForm(instance = todo, data = request.POST)
		# Check if valid, then save 
		if form.is_valid():
			form.save() 
			# Redirect the user to the main todos page, 
			# or the todo itself?
		### TEST ###
		else: 
			# Printing to terminal for test 
			print("\nThis didn't pass...\n")
			# Add additional information and reload the page...

			# Here is how you would return back without an arg- it seems
			# that this function does not allow for the 'todo_id'
			# return HttpResponseRedirect(reverse('todos_main'))
			# Otherwise, the same as below should work...
		contents = {'todo': todo,'form': form}
		return render(request, 'todo/todo_details.html', contents)
		
	# remember to return form data, not JUST the model itself. 
	contents = {'todo': todo,'form': form}
	return render(request, 'todo/todo_edit.html', contents)

# NOTES FOR ABOVE todo_edit()
# You can move the individual return statements into the appropriate 
# conditional. A simple redirect could work too. 

def todo_create(request):
	"""Create a new ToDo entry."""
	if request.method != 'POST':
		form = ToDoForm()
	
	else:
		form = ToDoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('todos_main'))
	
	return render(request, 'todo/create_todo.html', {'form': form})





















