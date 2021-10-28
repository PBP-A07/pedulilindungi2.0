from django.db import models

# Create your models here.
class Vaksin(models.Model):
    jenis = models.CharField(max_length=30)
    tanggal = models.DateField()
    waktu = models.TimeField()
    jumlah = models.SmallIntegerField()