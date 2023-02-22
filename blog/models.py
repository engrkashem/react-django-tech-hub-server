from django.db import models
from users.models import User

# Create your models here.

class BlogModel(models.Model):
    blog_heading=models.CharField(max_length=200, blank=False, default='')
    user_email=models.EmailField(blank=False, default='', null=False)
    blog_body=models.TextField()
    liked=models.IntegerField(default=0)
    post_time=models.DateField(auto_now=True ,blank=True, editable=False)
    saved_by=models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.blog_heading
