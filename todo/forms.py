# todo\forms.py 
# 04.30.2019 

from django import forms 

from .models import ToDo 

class ToDoForm(forms.ModelForm):
	"""Form for the ToDo model."""
	# Create the structure in a Meta class 
	class Meta: 
		model = ToDo 
		# fields as list 
		fields = [
			'title',
			'summary',
			'date_due', 
			'difficulty', 
		]
		# labels as dcny 
		labels = {
			'title': 'Title',
			'summary': 'Summary', 
			'date_due': 'Due Date',
			'difficulty': 'Level of Difficulty', 
		}
		# Widgets so that summary can be edited as a textarea, 
		# not a type='text' field. 
		widgets = {'summary': forms.Textarea(
			attrs = {'cols': 80, 'rows': 8}
			)
		}
