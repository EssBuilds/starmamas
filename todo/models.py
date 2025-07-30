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
    # Temporarily commenting out age and created_at fields until migration is applied
    # age = models.PositiveIntegerField(
    #     null=True,
    #     blank=True,
    #     help_text="The age of the child (optional)."
    # )
    # created_at = models.DateTimeField(
    #     auto_now_add=True,
    #     help_text="Timestamp when the child record was created."
    # )

    def save(self, *args, **kwargs):
        """
        Custom save method to handle database schema mismatch
        """
        from django.db import connection
        from django.utils import timezone
        
        # Check if age column exists before trying to save
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='todo_child' AND column_name='age'
            """)
            age_exists = cursor.fetchone() is not None
            
        if not age_exists:
            # If age column doesn't exist, save manually with only existing fields
            if not self.pk:  # New record
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO todo_child (user_id, name, created_at) VALUES (%s, %s, %s) RETURNING id",
                        [self.user_id, self.name, timezone.now()]
                    )
                    self.pk = cursor.fetchone()[0]
            else:  # Update existing record
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE todo_child SET name = %s WHERE id = %s",
                        [self.name, self.pk]
                    )
        else:
            # Normal save if all columns exist
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

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

