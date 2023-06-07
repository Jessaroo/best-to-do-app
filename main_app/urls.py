from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/',views.tasks_index, name='index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    # path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    # path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
]