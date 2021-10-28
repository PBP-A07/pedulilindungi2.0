from django.urls import path
from .views import daftar_vaksin, load_tanggal, load_jenis ,load_tempat

urlpatterns = [
    path('', daftar_vaksin, name='daftar-vaksin'),
    path('ajax/load-tanggal', load_tanggal, name='ajax-load-tanggal'),
    path('ajax/load-jenis', load_jenis, name='ajax-load-jenis'),
    path('ajax/load-tempat', load_tempat, name='ajax-load-tempat')
]

