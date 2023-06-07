from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    todo = models.CharField(max_length=50)
    when = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.color} {self.name}'
    
    def get_absolute_url(self):
        return reverse('tasks_detail', kwargs={'pk': self.id})
