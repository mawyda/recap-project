# recap\views.py
# 04.10.2019

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render(request, 'home.html')

@login_required
def count(request):
	fulltext = request.GET['fulltext']
	return render(request, 'count.html', {'text': fulltext})

@login_required
def code(request):
	return render(request, 'code.html')
