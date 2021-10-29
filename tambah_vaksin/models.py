from django.db import models

# Create your models here.
<<<<<<< HEAD
class Vaksin(models.Model):
    jenis = models.CharField(max_length=30)
    tanggal = models.DateField(blank=False, null=True)
    waktu = models.TimeField()
    jumlah = models.SmallIntegerField()
    penyedia = models.ForeignKey(Penyedia, on_delete=models.CASCADE, null=True, blank=True)
=======
>>>>>>> parent of b3c55a2 (Merge pull request #17 from PBP-A07/daftar-vaksin)
