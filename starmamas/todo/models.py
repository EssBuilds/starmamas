from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
