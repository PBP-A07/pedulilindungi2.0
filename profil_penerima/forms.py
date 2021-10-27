from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import widgets
from .models import Message

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