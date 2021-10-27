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
    kota = Penyedia.objects.get(pk=request.GET.get('kota_pk'))
    # kota_id = request.GET.get('penyedia')
    # tempats = Penyedia.objects.filter(kota_id=kota_id).values_list(
    #     'namaInstansi', flat=True).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'kota': kota})
