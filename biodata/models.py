from django import db
from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

class Peserta(models.Model):
    namaLengkap = models.CharField(max_length=25)
    NIK = models.CharField(max_length=16,unique=True)
    tanggalLahir = models.DateField()
    jenisKelamin = models.CharField(max_length=10)
    nomorHandphone = models.CharField(max_length=12)
    alamat = models.CharField(max_length=100)
    superUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Penyedia(models.Model):
    namaInstansi = models.CharField(max_length=50, unique=True)
    kota = models.CharField(max_length=20)
    nomorTelepon = models.CharField(max_length=10)
    alamat = models.CharField(max_length=100)
    superUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_penyedia(sender, instance, created, **kwargs):
    if created and instance.profile.role == "penyedia":
        Penyedia.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_peserta(sender, instance, created, **kwargs):
    if created and instance.profile.role == "penerima":
        Peserta.objects.create(user=instance)
