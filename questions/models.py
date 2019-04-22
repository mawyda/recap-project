# questions\models.py 
# 04.11.2019


# Create your models here.
from django.db import models
from datetime import datetime

class Questions(models.Model):
	title = models.CharField(max_length = 60)
	summary = models.CharField(max_length = 400)
	topic = models.CharField(max_length = 30)
	# tags 
	date = models.DateTimeField(default = datetime.now)
	
	
