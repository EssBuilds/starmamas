from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_task/', views.add_task, name='add_task'),
    path('add_child/', views.add_child, name='add_child'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('edit_child/<int:child_id>/', views.edit_child, name='edit_child'),
    path('delete_child/<int:child_id>/', views.delete_child, name='delete_child'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'
    ), name='password_change'),
]