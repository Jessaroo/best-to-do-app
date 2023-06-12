from django.contrib import admin
from .models import Task, Quote, Category

# Register your models here.
admin.site.register([Task, Quote, Category])