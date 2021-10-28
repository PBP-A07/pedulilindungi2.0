from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import JadwalVaksin
from biodata.models import Penyedia

class DaftarVaksinForm(ModelForm):
    kota = forms.ModelChoiceField(queryset=Penyedia.objects.order_by('kota').values_list('kota', flat=True).distinct(),
                                    empty_label="Pilih kota tempat vaksinasi")
    tempat = forms.ModelChoiceField(queryset=Penyedia.objects.none(),
                                    empty_label="Pilih tempat vaksinasi")

    class Meta:
        model = JadwalVaksin
        fields = ('kota', 'tanggal', 'jenis_vaksin', 'tempat', 'waktu')

