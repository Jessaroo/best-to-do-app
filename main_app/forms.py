from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['todo', 'when']
        category = ['errands', 'home', 'finances', 'work', 'travel', 'hobbies']