from django.db import models

# Create your models here.

class ToDo(models.Model):
	"""Class representing the ToDo model."""
	title = models.CharField(max_length = 40)
	summary = models.CharField(max_length = 500)
	date_added = models.DateTimeField(auto_now_add = True)
	date_due = models.DateTimeField()
		
	# define the level of difficutly by the Field.choices attribute 
	# Note: The pairs have to be tuples, the parent 'name_choices' an 
	# iterable 
	diff_choices = (
		('EA', 'Easy'),
		('MD', 'Brave'),
		('HD', 'Jedi'),
	)
	difficulty = models.CharField(
			max_length = 2, 
			choices = diff_choices,
			# Should probably variablize this...
			default = diff_choices[1][0],
		)  
	
	# TODO: overdue, priority, group/ tagged, 
	done = models.BooleanField(default = False)
	
	
	def __str__(self):
		return self.title
