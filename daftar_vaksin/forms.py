from django import forms
from django.db.models import fields
from django.forms import ModelForm, CharField, DateField, TimeField
from .models import JadwalVaksin

KOTA = []
JENIS_VAKSIN = []
TANGGAL = []
TEMPAT = []
WAKTU = []

# class DropdownChar(CharField):
#     input_type = 'text'

# class DropdownDate(DateField):
#     input_type = 'date'

# class DropdownTime(TimeField):
#     input_type = 'time'

class DaftarVaksinForm(ModelForm):
    # kota = forms.Select(choices=KOTA)
    # tanggal = forms.Select(choices=TANGGAL)
    # jenis_vaksin = forms.Select(JENIS_VAKSIN)
    # tempat = forms.Select(TEMPAT)
    # waktu = forms.Select(WAKTU)
    class Meta:
        model = JadwalVaksin
        fields = ['kota', 'tanggal', 'jenis_vaksin', 'tempat', 'waktu']
    #     widgets = {'kota': DropdownChar(attrs={'placeholder': 'Kota Tempat Vaksin'}, widget=forms.Select(choices=KOTA)),
    #                'tanggal': DropdownChar(attrs={'placeholder': 'Tanggal Vaksinasi'}, widget=forms.Select(choices=TANGGAL)), 
    #                'jenis_vaksin': DropdownChar(attrs={'placeholder': 'Jenis Vaksin'}, widget=forms.Select(JENIS_VAKSIN)), 
    #                'tempat': DropdownChar(attrs={'placeholder': 'Tempat Vaksinasi'}, widget=forms.Select(TEMPAT)),
    #                'waktu': DropdownChar(attrs={'placeholder': 'Waktu Vaksinasi'}, widget=forms.Select(WAKTU))}
