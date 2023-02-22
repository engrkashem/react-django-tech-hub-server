from django.db import models
from users.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo_url = models.URLField(blank=True)
    creator = models.ForeignKey(User, related_name="job_posted", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    