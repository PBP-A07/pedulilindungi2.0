from django import forms
from django.db.models import fields
from django.forms import ModelForm
from tambah_vaksin.models import Vaksin
from .models import JadwalVaksin
from biodata.models import Penyedia

class DaftarVaksinForm(ModelForm):
    kota_blank_choice = [('', 'Pilih kota tempat vaksinasi'), ]
    tanggal_blank_choice = [('', 'Pilih tanggal vaksinasi'), ]
    jenis_vaksin_blank_choice = [('', 'Pilih jenis vaksinasi'), ]
    tempat_blank_choice = [('', 'Pilih tempat vaksinasi'), ]
    kota_choice = [(i['kota'], i['kota']) for i in Penyedia.objects.values('kota').distinct()]
    kota = forms.ChoiceField(choices=kota_blank_choice + kota_choice, required=False)
    tanggal = forms.ChoiceField(choices=tanggal_blank_choice)
    jenis_vaksin = forms.ChoiceField(choices=jenis_vaksin_blank_choice)
    tempat = forms.ChoiceField(choices=tempat_blank_choice)

    class Meta:
        model = JadwalVaksin
        fields = ('kota', 'tanggal', 'jenis_vaksin', 'tempat')

