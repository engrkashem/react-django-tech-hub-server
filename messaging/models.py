from django.db import models
from users.models import User

# Create your models here.

class MessageModel(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    message_body=models.TextField()