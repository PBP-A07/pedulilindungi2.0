from django import forms
from django.forms import ModelForm
from .models import JadwalVaksin
from tambah_vaksin.models import Vaksin

def get_kota():
    return [('', 'Pilih kota tempat vaksinasi'), ] + [(i['penyedia__kota'], i['penyedia__kota']) for i in Vaksin.objects.values('penyedia__kota').exclude(jumlah=0).distinct()]

class DaftarVaksinForm(ModelForm):
    tanggal_blank_choice = [('', 'Pilih tanggal vaksinasi'), ]
    jenis_vaksin_blank_choice = [('', 'Pilih jenis vaksinasi'), ]
    tempat_blank_choice = [('', 'Pilih tempat vaksinasi'), ]
    kota = forms.ChoiceField(choices=get_kota, required=False)
    tanggal = forms.ChoiceField(choices=tanggal_blank_choice)
    jenis_vaksin = forms.ChoiceField(choices=jenis_vaksin_blank_choice)
    tempat = forms.ChoiceField(choices=tempat_blank_choice)

    class Meta:
        model = JadwalVaksin
        fields = ('kota', 'tanggal', 'jenis_vaksin', 'tempat')

