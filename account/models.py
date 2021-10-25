from django.db import models

# Create your models here.


class Penyedia(models.Model):
    email = models.EmailField(
        max_length=254)
    username = models.CharField(
        max_length=30)
    password = models.CharField(
        max_length=30)

    def __str__(self):
        return self.username


class Penerima(models.Model):
    email = models.EmailField(
        max_length=254)
    username = models.CharField(
        max_length=30)
    password = models.CharField(
        max_length=30)

    def __str__(self):
        return self.username
