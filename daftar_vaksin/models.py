from django.db import models
from django.http import request
from biodata.models import Penyedia, Peserta

class JadwalVaksin(models.Model):
   kota = models.CharField(max_length=30)
   tempat = models.ForeignKey(Penyedia, on_delete=models.CASCADE)
   tanggal = models.CharField(max_length=30, default='')
   jenis_vaksin = models.CharField(max_length=30, default='')
   waktu = models.CharField(max_length=30, default='')
   penerima = models.ForeignKey(Peserta, on_delete=models.CASCADE, null=True)

