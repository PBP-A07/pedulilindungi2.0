from django import forms
from django.db.models import fields
from django.forms import ModelForm
from tambah_vaksin.models import Vaksin
from .models import JadwalVaksin
from biodata.models import Penyedia

class DaftarVaksinForm(ModelForm):
    kota = forms.ModelChoiceField(queryset=Penyedia.objects.values_list('kota', flat=True).distinct(),
                                    empty_label="Pilih kota tempat vaksinasi")
    tanggal = forms.ModelChoiceField(queryset=Vaksin.objects.none(), empty_label="Pilih tanggal vaksinasi")
    jenis = forms.ModelChoiceField(queryset=Vaksin.objects.none(), empty_label="Pilih jenis vaksin")
    tempat = forms.ModelChoiceField(queryset=Penyedia.objects.none(),
                                    empty_label="Pilih tempat vaksinasi")

    class Meta:
        model = JadwalVaksin
        fields = ('kota', 'tanggal', 'jenis', 'tempat')

