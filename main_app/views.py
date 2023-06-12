from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from main_app.models import Task, Category, Quote
from django.urls import reverse_lazy
import requests
import random


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def tasks_index(request):
  tasks = Task.objects.filter(user=request.user)
  url = 'https://zenquotes.io/api/quotes/'
  response = requests.get(url)
  if response.status_code == 200:
      quotes = response.json()
  else:
      quotes = []
  random.shuffle(quotes)
  num_quotes_to_display = 2
  quotes = quotes[:num_quotes_to_display]
  
  context = {
    'tasks': tasks,
    'quotes': quotes,
  }
  return render(request, 'tasks/index.html', context)

@login_required 
def tasks_detail(request, pk):
  task = Task.objects.get(pk=pk)
  categories = Category.objects.all()
  return render(request, 'tasks/detail.html', {'task': task})

def signup(request):
  error_message = ''
  if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('about')
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
  fields = ['todo', 'when']

class TaskDelete(DeleteView):
  model = Task
  success_url = reverse_lazy('index')
  template_name = 'main_app/task_confirm_delete.html'

class QuoteList(ListView):
  model = Quote