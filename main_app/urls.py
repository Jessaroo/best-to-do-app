from django.urls import path
from . import views
from .views import CategoryCreate


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/',views.tasks_index, name='index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('tasks/<int:task_id>/add_category/', views.add_category, name='add_category'),
    path('tasks/<int:task_id>/remove_category/<int:category_id>/', views.remove_category, name='remove_category'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]