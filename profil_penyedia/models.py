from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class CatatanPenyedia(models.Model):
    title = models.TextField()
    message = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)