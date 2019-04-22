# questions/forms.py 
# 04.15.2019 

from django import forms

from .models import Questions

class QuestionForm(forms.ModelForm):
	class Meta:
		# Requires model, fields to edit of that model, and potentially
		# labels for the forms. 
		model = Questions 
		fields = ['title', 'summary', 'topic']
		labels = {'title': 'Title', 'summary': 'Summary', 
			'topic': 'Topics'}
		# widget to change the summary to a text area, so line breaks 
		# can be added.
		widgets = {'summary': forms.Textarea(attrs = 
			{'cols': 80, 'rows': 8})
		}
		# Trying to get CSS into the widget...
		#widgets = {'summary': forms.Textarea(attrs = 
		#	{'cols': 80, 'rows': 8, 'class': 'textarea-field'})
		#}
