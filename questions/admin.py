from django.contrib import admin

# Register your models here.
from .models import Questions

# IS this the name of the app or the model itself? 
admin.site.register(Questions) 

