from django.db import models
from users.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=50, default='')
    job_type = models.CharField(max_length=15, default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="job_posted", on_delete=models.CASCADE, default='')
    location = models.CharField(max_length=150, default='')
    skill_requirements = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
    