from django.db import models
from biodata.models import Penyedia

# Create your models here.
class Vaksin(models.Model):
    jenis = models.CharField(max_length=30)
<<<<<<< HEAD
    tanggal = models.DateField()
=======
    tanggal = models.DateField(blank=False, null=True)
    waktu = models.TimeField()
>>>>>>> fdebf8e278c4ffb3409c93fe2520ec961cbfd821
    jumlah = models.SmallIntegerField()
    penyedia = models.ForeignKey(Penyedia, on_delete=models.CASCADE, null=True, blank=True)
