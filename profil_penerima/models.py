from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    msg_title = models.CharField(max_length=100)
    msg_message = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)