from django.db import models
from django.http import request
from biodata.models import Penyedia, Peserta

class JadwalVaksin(models.Model):
   kota = models.CharField(max_length=30, default='')
   tanggal = models.CharField(max_length=30)
   jenis_vaksin = models.CharField(max_length=30)
   tempat = models.ForeignKey(Penyedia, on_delete=models.CASCADE)
   waktu = models.CharField(max_length=30)
   penerima = models.ForeignKey(Peserta, on_delete=models.CASCADE, null=True)

