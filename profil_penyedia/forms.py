from django import forms
from django.forms import widgets
from biodata.models import Penyedia

class EditPenyediaForm(forms.ModelForm):
    class Meta:
        model = Penyedia
        fields = ['namaInstansi', 'kota', 'nomorTelepon', 'alamat']
        widgets = {
            'namaInstansi': forms.TextInput(attrs={'class': 'form_input', 'placeholder': "Masukkan nama instansi kamu"}),
            'kota': forms.TextInput(attrs={'class': 'form_input', 'placeholder': "Masukkan kota instansi kamu"}),
            'nomorTelepon': forms.TextInput(attrs={'class': 'form_input', 'placeholder': "Masukkan nomor telepon instansi kamu"}),
            'alamat': forms.TextInput(attrs={'class': 'form_input', 'placeholder': "Masukkan alamat instansi kamu"})
        }
