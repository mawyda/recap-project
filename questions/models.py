# questions\models.py 
# 04.11.2019


# Create your models here.
from django.db import models
from datetime import datetime

class Questions(models.Model):
	title = models.CharField(max_length = 60)
	summary = models.CharField(max_length = 1200)
	topic = models.CharField(max_length = 30)
	# tags 
	date = models.DateTimeField(default = datetime.now)
	
	def __str__(self):
		#return self.title[:20] + "..."
		return self.title
		
class Tags(models.Model):
	"""Class for tags for entries."""
	title = models.CharField(max_length = 35) 
	questions = models.ManyToManyField(Questions)	
	# How to return the number of questions the tag is related to? 
	# ...Each model is row...or does this more refer to a table? 
	
	def __str__(self):
		return self.title	
	
