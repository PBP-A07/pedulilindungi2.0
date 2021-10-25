from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('peserta_form', biodata_peserta, name='peserta'), 
    path('penyedia_form', biodata_penyedia, name='penyedia'), # ubah method jadi 1 biar bisa make modul ricky
    path('peserta/create', ajax_posting_peserta),
    path('penyedia/create', ajax_posting_penyedia),
]
