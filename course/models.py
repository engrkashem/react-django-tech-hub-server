from django.db import models
from django import forms
from users.models import User

class Course(models.Model):

    instructor = models.ForeignKey(User, related_name='instructor', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    description = models.TextField()
    course_fee = models.IntegerField( default=0)
    course_length = models.CharField(max_length=200, default='')
    video_thumbnail_url = models.CharField(max_length=200, default='')
    video_playlist_url = models.CharField(max_length=200, default='')
    enroll_status=models.BooleanField( default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Enroll(models.Model):
    student = models.ForeignKey(User, related_name='Enroll_User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='Enroll_Course', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.title


# "2022-03-09 10:00:00+05:30"
