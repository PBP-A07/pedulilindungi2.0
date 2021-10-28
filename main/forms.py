from django.forms import widgets
from .models import Discussion, Questions
from django import forms

class NewQuestion(forms.ModelForm) :
    class Meta :
        model = Questions
        fields = ['title', 'body']
    title_attrs = {
        'type' : 'text',
        'placeholder' : 'Ketikkan judul forum',
    }
    title = forms.CharField(label='title', required=True, widget=forms.TextInput(attrs=title_attrs))

class NewResponse(forms.ModelForm) :
    class Meta :
        model = Discussion
        fields = ['body']
        widgets = {
                'body' : forms.Textarea(attrs={
                'rows' : 2,
                'placeholder' : "Tulis tanggapan Anda"
            })
        }

class NewReply(forms.ModelForm) :
    class Meta :
        model = Discussion
        fields = ['body']
        widgets = {
                'body' : forms.Textarea(attrs={
                'rows' : 2,
                'placeholder' : "Tulis tanggapan Anda"
            })
        }