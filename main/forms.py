from django.forms import widgets
from .models import Discussion, Questions
from django import forms

class NewQuestion(forms.ModelForm) :
    class Meta :
        model = Questions
        fields = ['title', 'body']

class NewResponse(forms.ModelForm) :
    class Meta :
        model = Discussion
        fields = ['body']

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