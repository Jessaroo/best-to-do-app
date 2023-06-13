from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Quote(models.Model):
    quote_text = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.quote_text
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
class Task(models.Model):
    todo = models.CharField(max_length=50)
    when = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.todo
    
    def get_absolute_url(self):
        return reverse('index')