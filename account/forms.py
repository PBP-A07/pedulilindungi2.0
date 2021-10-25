from django import forms
from django.forms import widgets
from .models import Penerima, Penyedia

ROLE_CHOICES = [
    ('penerima', 'Penerima'),
    ('penyedia', 'Penyedia'),
]


class RadioForm(forms.Form):
    role_choice = forms.CharField(
        label="Saya adalah", widget=forms.RadioSelect(choices=ROLE_CHOICES))


class PenyediaForm(forms.ModelForm):
    class Meta:
        model = Penyedia
        fields = "__all__"
        widgets = {'password': forms.PasswordInput}


class PenerimaForm(forms.ModelForm):
    class Meta:
        model = Penerima
        fields = "__all__"
        widgets = {'password': forms.PasswordInput}
