from django.db import models
from biodata.models import Penyedia, Peserta

class JadwalVaksin(models.Model):
   kota = models.CharField(max_length=255)
   tanggal = models.DateField()
   jenis_vaksin = models.CharField(max_length=255, default='')
   place = models.ForeignKey(Penyedia, on_delete=models.CASCADE, null=True, blank=True)
   tempat = models.CharField(max_length=255)
   penerima = models.ForeignKey(Peserta, on_delete=models.CASCADE, null=True, blank=True)

