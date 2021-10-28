from django import forms
from biodata.models import Penyedia
from django.contrib.auth.models import User
from .models import CatatanPenyedia

class EditPenyediaForm(forms.ModelForm):
    class Meta:
        model = Penyedia
        fields = ['namaInstansi', 'kota', 'nomorTelepon', 'alamat']

class CatatanPenyediaForm(forms.ModelForm):
    class Meta:
        model = CatatanPenyedia
        fields = ['title', 'message']