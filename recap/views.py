# recap\views.py
# 04.10.2019

from django.shortcuts import render 

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	return render(request, 'count.html', {'text': fulltext})

def code(request):
	return render(request, 'code.html')

