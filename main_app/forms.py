from django import forms
from main_app.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['todo', 'when', 'category']
        