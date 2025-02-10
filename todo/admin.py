from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Child, Task

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'user', 'created_at')
    search_fields = ('name', 'user__username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'due_date', 'user', 'child', 'created_at')
    list_filter = ('priority', 'status', 'due_date')
    search_fields = ('title', 'user__username', 'child__name')