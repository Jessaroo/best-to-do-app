from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import DetailView
from main_app.models import Task, Category, FavoriteQuote, Quote
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from .forms import TaskForm
from django import forms
from django.forms import SelectMultiple
import requests
import random


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  tasks = Task.objects.all()
  url = 'https://zenquotes.io/api/quotes/'
  response = requests.get(url)
  if response.status_code == 200:
    quotes = response.json()
  else:
    quotes = []
    
  random.shuffle(quotes)
  num_quotes_to_display = 2
  quotes = quotes[:num_quotes_to_display]
  return render(request, 'tasks/index.html', {'tasks': tasks, 'quotes': quotes})
  
def tasks_detail(request, pk):
  task = Task.objects.get(pk=pk)
  categories = Category.objects.all()
  return render(request, 'tasks/detail.html', {'task': task, 'categories': categories})

def pending_tasks(request):
  return render(request, 'main_app/pending_tasks.html')
   
def add_category(request, task_id):
  task = Task.objects.get(id=task_id)
  if request.method == 'POST':
    category_id = request.POST.get('category_id')
    category = Category.objects.get(id=category_id)
    task.categories.add(category)
    return redirect('tasks_detail', task_id=task.id)
  categories = Category.objects.all()
  return render(request, 'add_category.html', {'task': task, 'categories': categories})
  
def remove_category(request, task_id, category_id):
  task = Task.objects.get(id=task_id)
  category = Category.objects.get(id=category_id)
  task.categories.remove(category)
  return redirect('tasks_detail', task_id=task.id)

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

class CategoryCreate(CreateView):
  model = Category
  fields = ['name']
  template_name = 'categories/category_form.html'

class CategoryList(View):
  def get(self, request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
  
class CategoryDetail(DetailView):
  model = Category
  template_name = 'categories/detail.html'
  context_object_name = 'category' 
  
class CategoryUpdate(UpdateView):
  model = Category
  fields = ['name']
  template_name = 'categories/category_form.html'
  
class CategoryDelete(DeleteView):
  model = Category
  success_url = reverse_lazy('category_list')
  template_name = 'categories/category_confirm_delete.html'
  context_object_name = 'category'
  
class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['todo', 'when', 'categories']
  
  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
  
  def get_form(self, form_class=None):
      form = super().get_form(form_class)
      form.fields['categories'].widget = forms.SelectMultiple()
      return form
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    return context
      
class TaskUpdate(UpdateView):
  model = Task
  form_class = TaskForm
  template_name = 'tasks/task_form.html'
  success_url = reverse_lazy('tasks_index')

class TaskDelete(DeleteView):
  model = Task
  success_url = reverse_lazy('tasks_index')
  template_name = 'tasks/task_confirm_delete.html'
    
  def delete(self, request, *args, **kwargs):
      self.object = self.get_object()
      success_url = self.get_success_url()
      self.object.delete()
      return HttpResponseRedirect(success_url)
    
def Quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes.html', {'quotes': quotes})
    
def random_quotes(request):
  url = 'https://zenquotes.io/api/quotes/'
  response = requests.get(url)
  if response.status_code == 200:
      quotes = response.json()
  else:
      quotes = []
 
  if request.method == 'POST':
      quote_id = request.POST.get('quote_id')
      selected_quote = quotes[int(quote_id)]
      FavoriteQuote.objects.create(
        quote=selected_quote['q'],
        author=selected_quote['a'],
        user=request.user
      )
      return redirect('favorite_quotes')
  return render(request, 'quotes.html')

def save_quote(request):
    if request.method == 'POST':
        quote_text = request.POST.get('quote')
        author_text = request.POST.get('author')
        user = request.user
      
        favorite_quote = FavoriteQuote(
            quote=quote_text,
            author=author_text,
            user=user
        )
        favorite_quote.save()
    return redirect('favorite_quotes')

def favorite_quotes(request):
  user = request.user
  favorite_quotes = FavoriteQuote.objects.filter(user=user)
  url = 'https://zenquotes.io/api/quotes/'
  response = requests.get(url)
  if response.status_code == 200:
      quotes = response.json()
  else:
      quotes = []  
  return render(request, 'favorite_quotes.html', {'favorite_quotes': favorite_quotes, 'quotes': quotes })