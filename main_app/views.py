from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import DetailView
from .models import Task, Category

# dummy tasks
tasks = [
    {'todo': 'wash towels', 'when': 'Today'},
    {'todo': 'wash dishes', 'when': 'Tonight'},
]

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
    
def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return reirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'signup.html', {'form': form})
