from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Task, Child
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskForm, ChildForm, RegisterForm

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        children = Child.objects.filter(user=request.user).only('id', 'user_id', 'name')
        return render(request, 'account/home.html', {'tasks': tasks, 'children': children})
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('todo:home')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect('todo:home')
        messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('todo:login')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added!")
            return redirect('todo:home')
    elif request.method == 'GET':
        form = TaskForm()
        return render(request, 'account/add_task.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated!")
            return redirect('todo:home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'account/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted!")
        return redirect('todo:home')
    return HttpResponseNotAllowed(['POST'])

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})