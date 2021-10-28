from django.urls import path
from .views import profil_penyedia, ubah_data_penyedia, lihat_pendaftar, catatan_penyedia, tambah_catatan

urlpatterns = [
    path('', profil_penyedia),
    path('ubah-data-penyedia', ubah_data_penyedia),
    path('lihat-pendaftar', lihat_pendaftar),
    path('catatan-penyedia', catatan_penyedia),
    path('tambah-catatan', tambah_catatan),
]