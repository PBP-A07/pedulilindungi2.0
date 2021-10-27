from django import forms
from django.db.models import fields
from django.forms import ModelForm, CharField, DateField, TimeField, widgets
from .models import JadwalVaksin
from biodata.models import Penyedia

class DaftarVaksinForm(ModelForm):
    kota = forms.ModelChoiceField(queryset=Penyedia.objects.order_by('kota').values_list('kota', flat=True).distinct())
    tempat = forms.ModelChoiceField(queryset=Penyedia.objects.none())

    class Meta:
        model = JadwalVaksin
        fields = ('kota', 'tanggal', 'jenis_vaksin', 'tempat', 'waktu')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['kota'].queryset = Penyedia.objects.all().values_list('kota', flat=True)
        # self.fields['tanggal'].queryset = Penyedia.objects.none().values_list('tanggal', flat=True)
        # self.fields['jenis_vaksin'].queryset = Penyedia.objects.none().values_list('jenis_vaksin', flat=True)
        self.fields['tempat'].queryset = Penyedia.objects.none().values_list('namaInstansi', flat=True)
        # self.fields['waktu'].queryset = Penyedia.objects.none().values_list('waktu', flat=True)

        if 'kota' in self.data:
            try:
                kota_get = self.data.get(kota='kota')
                self.fields['tempat'].queryset = Penyedia.objects.filter(kota_get=kota_get).values_list('namaInstansi', flat=True).distinct()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['tempat'].queryset = self.instance.kota.namaInstansi_set
