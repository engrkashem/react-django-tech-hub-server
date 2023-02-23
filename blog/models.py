from django.db import models
from users.models import User

# Create your models here.

class BlogModel(models.Model):
    blog_heading=models.CharField(max_length=200, blank=False, default='')
    blog_body=models.TextField()
    post_time=models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    post_update_time=models.DateTimeField(auto_now=True, blank=True, editable=False)
    img_url=models.URLField(blank=True)
    blog_creator=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')   
    liked=models.IntegerField(default=0)
    saved_by=models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.blog_heading
