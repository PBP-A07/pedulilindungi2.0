from django.db import models

KOTA = []
JENIS_VAKSIN = []
TANGGAL = []
TEMPAT = []
WAKTU = []

class JadwalVaksin(models.Model):
   kota = models.CharField(max_length=30, choices=KOTA)
   tanggal = models.CharField(max_length=30, choices=TANGGAL)
   jenis_vaksin = models.CharField(max_length=30, choices=JENIS_VAKSIN)
   tempat = models.CharField(max_length=30, choices=TEMPAT)
#    tempat = models.ForeignKey(Penyedia, on_delete=models.CASCADE)
   waktu = models.CharField(max_length=30, choices=WAKTU)
   # penerima = models.ForeignKey(Penerima, db_column="Penerima.NIK", on_delete=models.CASCADE)

