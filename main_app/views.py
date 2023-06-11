from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Task, Category
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from .forms import TaskForm
import requests
import random


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', {'tasks': tasks})
  
def tasks_detail(request, pk):
  task = Task.objects.get(pk=pk)
  categories = Category.objects.all()
  return render(request, 'tasks/detail.html', {'task': task})

@csrf_protect
def signup(request):
  error_message = ''
  if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('index')
  else:
      error_message = 'Invalid signup - try again'
        
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error': error_message
  })
  
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['todo', 'when']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
      
class TaskUpdate(UpdateView):
  model = Task
  form_class = TaskForm
  template_name = 'tasks/task_form.html'
  success_url = reverse_lazy('tasks_index')

class TaskDelete(DeleteView):
  model = Task
  success_url = reverse_lazy('tasks_index')
  template_name = 'tasks/task_confirm_delete.html'
  
def random_quotes(request):
    url = 'https://zenquotes.io/api/quotes/'
    response = requests.get(url)
    if response.status_code == 200:
      quotes = response.json()
    else:
      quotes = []
    random.shuffle(quotes)
    num_quotes_to_display = 2
    quotes = quotes[:num_quotes_to_display]
    
    return quotes