# questions\urls.py
# 04.11.2019

from django.contrib import admin #is this really necessary?
from django.urls import path

from . import views

urlpatterns = [
	path('', views.allquestions, name = 'allquestions'),
	path('<int:q_id>/', views.details, name = 'details'),
	path('edit_entry/<int:q_id>/', views.edit_entry, 
			name = 'edit_entry'),
	path('new_entry/', views.new_entry, name = 'new_entry'),
]


# Notes: 
# had an issue with a space inbetween int: and the variable
# That's ridiculous, but it worked. 
