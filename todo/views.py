# todo\views.py
# 04.30.2019


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from datetime import datetime
import pytz

from .models import ToDo
from .forms import ToDoForm

@login_required
def todos(request):
	"""Home page of the todos app."""

	# Notes:
	'''
	Will the incomplete item count be made redundant once the filter
	is applied and only unfinished items exist? Probably...
	'''


	# All data can be grabbed upfront, or the all() method used in
	# template
	todos = ToDo.objects.all()
	# Filtering for counts of Overdue and Incomplete
	# Q?: Should overdue be a model field, or done on the fly?
	# Q?: Should this be dumped in a utils file?

	incomplete = ToDo.objects.filter(done = False)
	# for now, getting a count of overdue items
	now = datetime.now(tz = pytz.utc) # Should be more accurate like EST
	counter = 0
	for t in incomplete: # do not care about finished ToDos
		if now > t.date_due:
			counter += 1

	# Using a template filter to provide len() of incomplete.
	# Also, should a single query object be passed, and then the various
	# filters done in the template? Question entry...

	context = {'todos': todos, 'inc' : incomplete, 'overdue': counter}
	return render(request, 'todo/todos_main.html', context)

@login_required
def todo_details(request, todo_id):
	"""The individual detail page for the ToDo items"""
	# the "read" portion of crud
	todo = ToDo.objects.get(id = todo_id)
	# Steps for deleting entries
	if request.method == 'POST':
		# JS added to prompt user.
		# The odsy queryset has the key: value pair corresponding to the html's
		# Values of the name and value attributes, so
		# <name = "submit" value = "delfrm1"
	
		if request.POST['submit'] == 'delfrm1':
			# Delete entry, return to main ToDo page.
			todo.delete()
			# TODO: Use the built in messages class to pass info
			return HttpResponseRedirect(reverse('todos_main'))

	# Otherwise, display the data
	return render(request, 'todo/todo_details.html', {'todo': todo})

@login_required
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

			# Here is how you would return back without an arg- it
			# seems that this function does not allow for the
			# 'todo_id'
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

@login_required
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
