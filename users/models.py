from django.db import models

# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    photo_url=models.CharField(max_length=500, blank=True)
    skill_set=models.CharField(max_length=500, blank=True)
    profession=models.CharField(max_length=500, blank=True)
    user_role=models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.email

