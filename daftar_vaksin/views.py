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
    kota_id = request.GET.get('id')
    tanggal = Vaksin.objects.filter(penyedia_id=kota_id).values_list(
        'tanggal', flat=True).distinct()
    return render(request, 'hr/tanggal_dropdown.html', {'tanggal': tanggal})

def load_jenis_vaksin(request):
    tanggal_id = request.GET.get('tanggal')
    jenis_vaksin = Vaksin.objects.filter(tanggal=tanggal_id).values_list('jenis', flat=True).distinct()
    return render(request, 'hr/jenis_dropdown.html', {'jenis_vaksin': jenis_vaksin})

def load_tempat(request):
    tanggal_id = request.GET.get('tanggal')
    jenis_id = request.GET.get('jenis')
    tempat = Vaksin.objects.filter(tanggal=tanggal_id, jenis=jenis_id).values_list('penyedia', flat=True).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})

