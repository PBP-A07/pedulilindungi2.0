from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DaftarVaksinForm
from biodata.models import Penyedia
from tambah_vaksin.models import Vaksin

# Create your views here.
def daftar_vaksin(request):
    form = DaftarVaksinForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST' and request.user.is_authenticated()):
        jadwal = form.save(commit=False)
        jadwal.penerima = request.user
        jadwal.save()
        return HttpResponseRedirect('')
    else:
        form = DaftarVaksinForm()

    return render(request, 'daftar_vaksin.html', {'form': form})


def load_tanggal(request):
    kota_id = request.GET.get('kota')
    tanggal = Vaksin.objects.filter(kota_id=kota_id).values_list(
        'tanggal', flat=True).distinct()
    return render(request, 'hr/tanggal_dropdown.html', {'tanggal': tanggal})

def load_jenis(request):
    kota_id = request.GET.get('kota')
    tanggal_id = request.GET.get('tanggal')
    jenis = Vaksin.objects.filter(kota_id=kota_id, tanggal=tanggal_id).values_list('jenis', flat=True).distinct()
    return render(request, 'hr/jenis_dropdown.html', {'jenis': jenis})

def load_tempat(request):
    kota_id = request.GET.get('kota')
    tanggal_id = request.GET.get('tanggal')
    jenis_id = request.GET.get('jenis')
    tempat = Vaksin.objects.filter(kota=kota_id, tanggal=tanggal_id, jenis=jenis_id).values_list('penyedia', flat=True).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})

