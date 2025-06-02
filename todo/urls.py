<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
=======
from django.urls import path, include
>>>>>>> f1102da3c10db0bb8e4b703db33660f03903f3c3
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
<<<<<<< HEAD
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'
    ), name='password_change'),
=======
>>>>>>> f1102da3c10db0bb8e4b703db33660f03903f3c3
]