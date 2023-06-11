from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks_index, name='index'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('quotes/', views.random_quotes, name='quotes_list'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
]

# path('quotes/', views.QuoteList.as_view(), name='quotes_list'),