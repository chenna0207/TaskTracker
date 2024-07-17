from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

class UserProjectRole(models.Model):
    ROLE= [
        ('admin', 'Admin'),
        ('task_creator', 'Task Creator'),
        ('read_only', 'Read Only'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE)

    class Meta:
        unique_together = ('user', 'project', 'role')

class Task(models.Model):
    TASK_STATUS = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
        ('not_started', 'Not Started'),
    ]

    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=TASK_STATUS, default='not_started')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')



