from django.urls import path
from .views import tambah_vaksin, load_jenis_vaksin, load_tanggal, load_tempat

urlpatterns = [
    path('', tambah_vaksin, name='tambah-vaksin'),
    path('ajax/load-tanggal', load_tanggal, name='ajax-load-tanggal'),
    path('ajax/load-jenis-vaksin', load_jenis_vaksin,
         name='ajax-load-jenis-vaksin'),
    path('ajax/load-tempat', load_tempat, name='ajax-load-tempat')
]