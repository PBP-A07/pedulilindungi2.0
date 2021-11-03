from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.core import serializers
from tambah_vaksin.forms import VaccineForm
from tambah_vaksin.models import Vaksin

def add_vaccine(request):
    form = VaccineForm(request.POST or None)
    vaccine = Vaksin.objects.all()
    response = {'vaccine':vaccine}  
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return render(request, 'daftar_vaksin.html', response)
    else:
        return render(request, 'tambahvaksin_index.html', {'form': form})
