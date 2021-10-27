from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DaftarVaksinForm
from biodata.models import Penyedia

# Create your views here.
def daftar_vaksin(request):
    form = DaftarVaksinForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('')
    else:
        form = DaftarVaksinForm()

    return render(request, 'daftar_vaksin.html', {'form': form})

def load_tempat(request):
    kota_id = request.GET.get('kota')
    tempat = Penyedia.objects.filter(kota=kota_id).values_list('namaInstansi', flat=True).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})
