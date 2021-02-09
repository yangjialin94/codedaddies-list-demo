from django.contrib import admin

# bring in our models
from .models import Search

# Register your models here.
admin.site.register(Search)
