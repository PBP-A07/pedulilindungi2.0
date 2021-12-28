from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('user/<usn>', profil_penyedia, name='profil_penyedia'),
    path('ubah-data-penyedia', ubah_data_penyedia, name='ubah_data_penyedia'),
    path('lihat-pendaftar', lihat_pendaftar, name='lihat_pendaftar'),
    path('catatan-penyedia', catatan_penyedia, name='catatan_penyedia'),
    path('tambah-catatan', tambah_catatan, name='tambah_catatan'),
    path('catatan-penyedia-json', json_catatan_penyedia, name='json_catatan_penyedia'),
    path('profil-penyedia-json', json_profil_penyedia, name='json_profil_penyedia'),
    path('lihat-pendaftar-json', json_lihat_pendaftar, name='json_lihat_pendaftar'),
    path('catatan-penyedia-flutter', flutter_catatan_penyedia, name='flutter_catatan_penyedia'),
    # path('profil-penyedia-flutter', flutter_profil_penyedia, name='flutter_profil_penyedia')
]