from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import DetailView
from .models import Task, Category
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

# dummy tasks
tasks = [
    {'todo': 'wash towels', 'when': 'Today'},
    {'todo': 'wash dishes', 'when': 'Tonight'},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', {'tasks': tasks})
  
def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', {'task': task})
  
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
  model = Categoryfields = ['name']
  fields = ['name']
  template_name = 'categories/category_form.html'
  
class CategoryDelete(DeleteView):
  model = Category
  success_url = reverse_lazy('category_list')
  template_name = 'categories/category_confirm_delete.html'
  contect_object_name = 'category'
  
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