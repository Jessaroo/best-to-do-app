from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    errands = models.CharField(max_length=50)
    home = models.CharField(max_length=50)
    finances = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    travel = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.color} {self.name}'
    
    def get_absolute_url(self):
        return reverse('caetgory_detail', kwargs={'pk': self.id})

class Task(models.Model):
    todo = models.CharField(max_length=50)
    when = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.color} {self.name}'
    
    def get_absolute_url(self):
        return reverse('tasks_detail', kwargs={'pk': self.id})
