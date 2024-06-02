from django.db import models

# Create your models here.

class TodoItem(models.Model):   
    content = models.TextField(max_length=255)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default=False)
    id = models.UUIDField(primary_key=True)