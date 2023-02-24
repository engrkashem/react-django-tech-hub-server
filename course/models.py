from django.db import models
from users.models import User

class Course(models.Model):
    instructor = models.ForeignKey(User, related_name='instructor', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_fee = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    course_length = models.CharField(max_length=200)
    video_thumbnail_url = models.CharField(max_length=200)
    video_playlist_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title