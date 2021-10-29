from django.db import models
from django.http import request
from biodata.models import Penyedia, Peserta

class JadwalVaksin(models.Model):
   kota = models.CharField(max_length=30)
   tanggal = models.DateField(blank=False, null=True)
   jenis_vaksin = models.CharField(max_length=30, default='')
   place = models.ForeignKey(Penyedia, on_delete=models.CASCADE, null=True)
   tempat = models.CharField(max_length=30)
   penerima = models.ForeignKey(Peserta, on_delete=models.CASCADE, null=True)

# Create your models here.
