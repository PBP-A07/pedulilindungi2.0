from django.urls import path
from .views import *

urlpatterns = [
    path('peserta_form', biodata_peserta, name='peserta'), 
    path('penyedia_form', biodata_penyedia, name='penyedia'),
    path('peserta/create', ajax_posting_peserta),
    path('penyedia/create', ajax_posting_penyedia)
]
