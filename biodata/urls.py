from django.urls import path
from .views import biodata_peserta, biodata_penyedia, ajax_posting_peserta, ajax_posting_penyedia, peserta_flutter, penyedia_flutter

urlpatterns = [
    path('peserta_form', biodata_peserta, name='peserta_form'), 
    path('penyedia_form', biodata_penyedia, name='penyedia_form'),
    path('peserta/create', ajax_posting_peserta, name='ajax_posting_peserta'),
    path('penyedia/create', ajax_posting_penyedia, name='ajax_posting_penyedia'),
    path('peserta/flutter', peserta_flutter, name='peserta_flutter'),
    path('penyedia/flutter', penyedia_flutter, name='penyedia_flutter'),
]
