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
        tasks = Task.objects.filter(user=request.user).select_related('child').order_by('-created_at')
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
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            # Debug: Print which child was assigned
            if task.child:
                messages.success(request, f"Task '{task.title}' added and assigned to {task.child.name}!")
            else:
                messages.success(request, f"Task '{task.title}' added!")
            return redirect('todo:home')
        else:
            # Debug: Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    elif request.method == 'GET':
        form = TaskForm(user=request.user)
        # Debug: Check if user has children
        children_count = request.user.children.count()
        if children_count == 0:
            messages.info(request, "You haven't added any family members yet. Add family members to assign tasks to them.")
        return render(request, 'account/add_task.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            updated_task = form.save()
            # Debug: Print which child was assigned
            if updated_task.child:
                messages.success(request, f"Task '{updated_task.title}' updated and assigned to {updated_task.child.name}!")
            else:
                messages.success(request, f"Task '{updated_task.title}' updated!")
            return redirect('todo:home')
        else:
            # Debug: Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = TaskForm(instance=task, user=request.user)
        # Debug: Check if user has children
        children_count = request.user.children.count()
        if children_count == 0:
            messages.info(request, "You haven't added any family members yet. Add family members to assign tasks to them.")
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
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = request.user
            child.save()
            messages.success(request, "Family member added!")
            return redirect('todo:home')
    elif request.method == 'GET':
        form = ChildForm()
        return render(request, 'account/add_child.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@login_required
def edit_child(request, child_id):
    child = get_object_or_404(Child, id=child_id, user=request.user)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            messages.success(request, "Family member updated!")
            return redirect('todo:home')
    else:
        form = ChildForm(instance=child)
    return render(request, 'account/edit_child.html', {'form': form, 'child': child})

@login_required
def delete_child(request, child_id):
    child = get_object_or_404(Child, id=child_id, user=request.user)
    if request.method == 'POST':
        child.delete()
        messages.success(request, "Family member removed!")
        return redirect('todo:home')
    return HttpResponseNotAllowed(['POST'])

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = not task.completed
        task.status = 'Completed' if task.completed else 'Pending'
        task.save()
        status_message = "marked as completed" if task.completed else "marked as pending"
        messages.success(request, f"Task '{task.title}' {status_message}!")
        return redirect('todo:home')
    return HttpResponseNotAllowed(['POST'])

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})