from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import HttpResponse
from django.core import serializers
from .forms import NoteForm
from lab_2.models import Note

def index(request):
    notes = Note.objects.all()
    response = {'notes' : notes}
    return render(request, 'lab4_index.html', response)

def add_note(request):
    form = NoteForm(request.POST or None)
    notes = Note.objects.all()
    response = {'notes':notes}  
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return render(request, 'lab4_index.html', response)
    else:
        return render(request, 'lab4_form.html', {'form': form})

def note_list(request):
    notes = Note.objects.all()
    response = {'notes' : notes}
    return render(request, 'lab4_note_list.html', response)