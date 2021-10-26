from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Peserta(models.Model):
    namaLengkap = models.CharField(max_length=25)
    NIK = models.IntegerField()
    tanggalLahir = models.DateField()
    jenisKelamin = models.CharField(max_length=10)
    nomorHandphone = models.IntegerField()
    alamat = models.CharField(max_length=100)

class Penyedia(models.Model):
    namaInstansi = models.CharField(max_length=50)
    kota = models.CharField(max_length=20)
    nomorTelepon = models.IntegerField()
    alamat = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_penyedia(sender, instance, created, **kwargs):
    if created and instance.profile.role == "penyedia":
        Penyedia.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_peserta(sender, instance, created, **kwargs):
    if created and instance.profile.role == "penerima":
        Peserta.objects.create(user=instance)