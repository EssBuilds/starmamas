# Description: Defines the models for the To-Do List app.

from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    """
    Represents a child associated with a user (e.g., family member).
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='children',  # Allows accessing children via user.children.all()
        help_text="The parent user who added this child."
    )
    name = models.CharField(
        max_length=100,
        help_text="The name of the child."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the child record was created.",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Task(models.Model):
    """
    Represents a task in the to-do list.
    """
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',  # Allows accessing tasks via user.tasks.all()
        help_text="The user who created the task."
    )
    child = models.ForeignKey(
        Child,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks',  # Allows accessing tasks via child.tasks.all()
        help_text="The child to whom the task is assigned (optional)."
    )
    title = models.CharField(
        max_length=255,
        help_text="A short description of the task."
    )
    description = models.TextField(
        blank=True,
        help_text="A detailed description of the task (optional)."
    )
    completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium',
        help_text="The priority level of the task."
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        help_text="The current status of the task."
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        help_text="The deadline for completing the task (optional)."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the task was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the task was last updated."
    )

    def __str__(self):
        return self.title

