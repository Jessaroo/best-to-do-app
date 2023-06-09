from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return {self.name}
    
    def get_absolute_url(self):
        return reverse('caetgory_detail', kwargs={'pk': self.id})

class Task(models.Model):
    todo = models.CharField(max_length=50)
    when = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return {self.todo}
    
    def get_absolute_url(self):
        return reverse('tasks_detail', kwargs={'pk': self.id})
    
class FavoriteQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.quote