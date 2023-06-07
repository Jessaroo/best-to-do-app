from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Task

# dummy tasks
tasks = [
    {'todo': 'wash towels', 'when': 'Today'},
    {'todo': 'wash dishes', 'when': 'Tonight'},
]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  return render(request, 'tasks/index.html', {
    'tasks': tasks
  })
  
def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', {'task': task})
  
class TaskCreate(CreateView):
  model = Task
  fields = ['todo', 'when']
  def form_valid(self, form):
        return super().form_valid(form)
      
class TaskUpdate(UpdateView):
    model = Task
    fields = ['todo', 'when']

class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasks/'
