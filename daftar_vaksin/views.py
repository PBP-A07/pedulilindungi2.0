from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from .forms import DaftarVaksinForm
from tambah_vaksin.models import Vaksin
from biodata.models import Penyedia, Peserta
from .models import JadwalVaksin


@login_required(login_url='/auth/login/')
def daftar_vaksin(request):
    # JadwalVaksin.objects.filter(tanggal__lt=date.today()).delete()
    person = Peserta.objects.get(superUser=request.user)
    form = DaftarVaksinForm(request.POST or None)

    if(JadwalVaksin.objects.filter(penerima=person).exists()):
        return HttpResponseRedirect('/profil-penerima/vaccine/ticket')
    else:
        kota = request.POST.get('kota')
        form.fields['kota'].choices = [(kota, kota)]

        tanggal = request.POST.get('tanggal')
        form.fields['tanggal'].choices = [(tanggal, tanggal)]

        jenis_vaksin = request.POST.get('jenis_vaksin')
        form.fields['jenis_vaksin'].choices = [(jenis_vaksin, jenis_vaksin)]

        tempat = request.POST.get('tempat')
        form.fields['tempat'].choices = [(tempat, tempat)]
        
        if (form.is_valid() and request.method == 'POST'):
            jadwal = form.save(commit=False)
            jadwal.place = Penyedia.objects.get(namaInstansi=jadwal.tempat)
            jadwal.penerima = person
            jadwal.save()
            vaksin = Vaksin.objects.get(penyedia=jadwal.place)
            vaksin.jumlah -= 1
            vaksin.save()
            return HttpResponseRedirect('/profil-penerima/vaccine/ticket')
        else:
            form = DaftarVaksinForm()

    return render(request, 'daftar_vaksin.html', {'form': form})


def load_tanggal(request):
    kota_id = request.GET.get('kota')
    tanggal = Vaksin.objects.filter(penyedia__kota=kota_id).values_list(
        'tanggal', flat=True).distinct()
    return render(request, 'hr/tanggal_dropdown.html', {'tanggal': tanggal})

def load_jenis_vaksin(request):
    tanggal_id = request.GET.get('tanggal')
    kota_id = request.GET.get('kota')
    jenis_vaksin = Vaksin.objects.filter(tanggal=tanggal_id, penyedia__kota=kota_id).values_list('jenis', flat=True).distinct()
    return render(request, 'hr/jenis_dropdown.html', {'jenis_vaksin': jenis_vaksin})

def load_tempat(request):
    jenis_id = request.GET.get('jenis_vaksin')
    tanggal_id = request.GET.get('tanggal')
    kota_id = request.GET.get('kota')
    tempat = Vaksin.objects.filter(
        jenis=jenis_id, tanggal=tanggal_id, penyedia__kota=kota_id).exclude(jumlah=0).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})

