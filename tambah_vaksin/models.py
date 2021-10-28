from django.db import models
from biodata.models import Penyedia

# Create your models here.
class Vaksin(models.Model):
    jenis = models.CharField(max_length=30)
    tanggal = models.DateField()
    waktu = models.TimeField()
    jumlah = models.SmallIntegerField()
    penyedia = models.ForeignKey(Penyedia, on_delete=models.CASCADE, null=True, blank=True)
