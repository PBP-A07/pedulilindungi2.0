from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import widgets

from account.models import Profile
from .models import Message
from biodata.models import Peserta
from account.models import Profile
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('Laki-Laki', 'Laki-Laki'),
    ('Perempuan', 'Perempuan')
]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields=['msg_title','msg_message']

        msg_title = forms.CharField(max_length='100', required=True)
        msg_message = forms.Textarea()

        labels = {
            'msg_title': _('Message Title'),
            'msg_message': _('Content'),
        }

        widgets = {
            'msg_message': forms.Textarea(),
        }

        error_messages = {
		    'required' : 'Input cannot be empty',
	    }

class DateInput(forms.DateInput):
    input_type = 'date'

class PenerimaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = ['namaLengkap','NIK','tanggalLahir','jenisKelamin','nomorHandphone','alamat']

        labels = {
            'namaLengkap': _('Nama Lengkap'),
            'NIK': _('Nomor Induk Kependudukan (NIK)'),
            'tanggalLahir': _('Tanggal Lahir'),
            'jenisKelamin': _('Jenis Kelamin'),
            'nomorHandphone': _('Nomor Handphone'),
            'alamat': _('Alamat'),
        }

        widgets = {
            'tanggalLahir': DateInput(),
            'jenisKelamin': forms.Select(choices = GENDER_CHOICES),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email']

        labels = {
            'email': _('Email'),
        }