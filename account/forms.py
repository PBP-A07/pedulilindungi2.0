from django import forms
from django.contrib.auth.forms import UserCreationForm


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
