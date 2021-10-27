from django.urls import path
from .views import profil_penyedia

urlpatterns = [
    path('', profil_penyedia)
    #path('ubah-data-penyedia', ubah_data_penyedia),
    #path('lihat-pendaftar', lihat_pendaftar),
]