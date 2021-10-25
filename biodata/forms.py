from django import forms
from .models import Peserta, Penyedia

GENDER_CHOICES = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan')
]

# buat user bisa milih tanggal-bulan-tahun
class DateInput(forms.DateInput): 
    input_type = 'date'

class PesertaForm (forms.ModelForm):
	class Meta:
		model = Peserta
		fields = "__all__"
		widgets = {
            'namaLengkap': forms.TextInput(attrs={'placeholder': 'Masukkan nama lengkap kamu', 
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1', 'id' : 'fullName'}),

            'NIK': forms.TextInput(attrs={'placeholder': 'Masukkan NIK kamu', 'type' : 'number', 
                        'maxlength': 16, 'minlength': 15,
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1', 'id' : 'nik'}),

            'tanggalLahir': forms.DateInput(attrs={'placeholder': 'Pilih tanggal lahir kamu',
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1',
                    'onclick':'(this.type="date")',
                    'onblur':"(this.type='text')",'id' : 'dob'}),

            'jenisKelamin': forms.Select(choices = GENDER_CHOICES, attrs={
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1','id' : 'gender'}),

            'nomorHandphone': forms.TextInput(attrs={'placeholder': 'Masukkan nomor handphone kamu', 'type' : 'number',
                        'maxlength': 12, 'minlength': 11,
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1','id' : 'hp'}),
                    
            'alamat': forms.TextInput(attrs={'placeholder': 'Masukkan alamat tinggal kamu',
                    'class' : 'inputan d-flex flex-column w-100 p-2 my-1', 'id' : 'address'})
        }
        # Set the fields attribute to the special value '__all__' 
        # to indicate that all fields in the model should be used.
	
class PenyediaForm (forms.ModelForm):
	class Meta:
		model = Penyedia
		fields = "__all__"
		widgets = {
            'namaInstansi': forms.TextInput(attrs={'placeholder': 'Masukkan nama instansi kamu', 
                        'class' : 'inputan d-flex flex-column w-100 p-2','id' : 'instansi'}),

            'kota': forms.TextInput(attrs={'placeholder': 'Masukkan kota instansi kamu',
                        'class' : 'inputan d-flex flex-column w-100 p-2','id' : 'city'}),

            'nomorTelepon': forms.TextInput(attrs={'placeholder': 'Masukkan nomor telepon instansi kamu',
                        'type' : 'number', 'maxlength': 10, 'size': 10, 'minlength': 9,
                        'class' : 'inputan d-flex flex-column w-100 p-2','id' : 'telp'}),

            'alamat': forms.TextInput(attrs={'placeholder': 'Masukkan alamat instansi kamu',
                        'class' : 'inputan d-flex flex-column w-100 p-2','id' : 'address'})
        }

# https://www.geeksforgeeks.org/how-to-set-placeholder-value-for-input-type-date-in-html-5/