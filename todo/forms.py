from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Child

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date', 'child']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']