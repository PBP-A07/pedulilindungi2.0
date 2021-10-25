from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile
from django.contrib.auth.models import User


ROLE_CHOICES = [
    ('penerima', 'Penerima'),
    ('penyedia', 'Penyedia'),
]


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254)

    # Radio button
    role_choice = forms.CharField(
        label="Saya adalah", widget=forms.RadioSelect(choices=ROLE_CHOICES))
