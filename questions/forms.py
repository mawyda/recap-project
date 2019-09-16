# questions/forms.py
# 04.15.2019

from django import forms
from pagedown.widgets import PagedownWidget

from .models import Questions

class QuestionForm(forms.ModelForm):
	# Override for pagedown
	summary = forms.CharField(widget = PagedownWidget())

	class Meta:
		# Requires model, fields to edit of that model, and potentially
		# labels for the forms.
		model = Questions
		fields = ['title', 'summary', 'topic']
		labels = {'title': 'Title', 'summary': 'Summary',
			'topic': 'Topics'}
