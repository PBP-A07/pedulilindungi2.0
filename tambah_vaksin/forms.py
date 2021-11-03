from django import forms
from tambah_vaksin.models import Vaksin

class VaccineForm(forms.ModelForm):
	class Meta:
		model = Vaksin
		fields = "__all__"
		widget = {
			'jenis' : forms.TextInput(attrs={'class': 'form-control'}),
    		'tanggal' : forms.TextInput(attrs={'class': 'form-control'}),
    		'jumlah' : forms.TextInput(attrs={'class': 'form-control'})
		}
