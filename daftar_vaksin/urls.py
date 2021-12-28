from django.urls import path
from .views import daftar_vaksin, daftar_vaksin_flutter, load_tanggal, load_jenis_vaksin, load_tempat

urlpatterns = [
    path('', daftar_vaksin, name='daftar-vaksin'),
    path('ajax/load-tanggal', load_tanggal, name='ajax-load-tanggal'),
    path('ajax/load-jenis-vaksin', load_jenis_vaksin,
         name='ajax-load-jenis-vaksin'),
    path('ajax/load-tempat', load_tempat, name='ajax-load-tempat'),
    path('daftar-vaksin/flutter', daftar_vaksin_flutter, name="daftar_vaksin_flutter")
]
