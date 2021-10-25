from django.db import models

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
