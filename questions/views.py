# questions\views.py
# 04.11.2019 

from django.shortcuts import render
from django.urls import reverse # For sending back to url...??? 
from django.http import HttpResponseRedirect # note above

# Import the models
from .models import Questions
from .forms import QuestionForm 

def allquestions(request):
	# Grab the object models 
	questions = Questions.objects
	# Pass the model as dcny
	return render(request, 'questions/allquestions.html', 
					{'questions': questions}
				)

def details(request, q_id):
	# Get the posting data by id number:
	q_details = Questions.objects.get(id = q_id)
	# return the data 
	return render(request, 'questions/details.html', 
				{'details': q_details})

def edit_entry(request, q_id):
	'''Edit entries and such.'''
	# init by getting the data from the model 
	entry = Questions.objects.get(id = q_id)
	
	# Check if post or get. 
	if request.method != 'POST':
		# No data submitted, return the prefilled form.
		# instance = entry will prefill the form.
		entry_form = QuestionForm(instance = entry)
		# return statement handled below (but why?. It could be here)
	else:
		# is POST so data submitted 
		# get the entry form data as object var 
		entry_form = QuestionForm(instance = entry, 
				data = request.POST) # Assumming the data contatins all
		
		# What does the is_valid() form actually check for? 
		# Also, there should be an else here if data is not entered 
		# correctly. DOes this method handle this stuff on its own? 
		if entry_form.is_valid():
			entry_form.save() # DB should be updated at this point.
			# Now redirtect back to the questions page. 
			# Although, it would be nice to see this done on the same
			# page. I wonder if this is JS? 
			
			return HttpResponseRedirect(reverse('allquestions'))
			
	# Return statement for the GET request
	return render(request, 'questions/edit_entry.html', 
		{'entry': entry, 'entry_form': entry_form}
	)

def new_entry(request): 
	'''Creates a new entry, versus using the admin/ site '''
	
	if request.method != 'POST':
		# Just serve up the page. 
		entry_form = QuestionForm()
	else: 
		# is the positional arg here actually kwarg : data
		entry_form = QuestionForm(request.POST)	
		if entry_form.is_valid():
			entry_form.save() 
			# TODO: add a msg saying this is done! 
			return HttpResponseRedirect(reverse('allquestions'))
	
	# Return the 'get' request portion 
	return render(request, 'questions/new_entry.html', 
			{'entry_form': entry_form}
		)
	










