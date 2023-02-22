from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_fee =models.IntegerField()
    video_thumbnail_url = models.CharField(max_length=200)
    video_playlist_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title