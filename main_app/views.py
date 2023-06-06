from django.shortcuts import render

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
