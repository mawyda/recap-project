from django.contrib import admin

# Register your models here.
from .models import Questions, Tags

# IS this the name of the app or the model itself? 
admin.site.register(Questions) 
admin.site.register(Tags)
