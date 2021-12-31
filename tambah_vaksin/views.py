# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, JsonResponse
from django.core import serializers
from tambah_vaksin.forms import VaccineForm
from tambah_vaksin.models import Vaksin
from biodata.models import Penyedia
from django.views.decorators.csrf import csrf_exempt
import json


@login_required(login_url='/auth/login/')
def tambah_vaksin(request):
    form = VaccineForm(request.POST or None)
    
    jenis = request.POST.get('jenis')
    form.fields['jenis'].choices = [(jenis, jenis)]

    tanggal = request.POST.get('tanggal')
    form.fields['tanggal'].choices = [(tanggal, tanggal)]

    jumlah1 = request.POST.get('jumlah')

    if (form.is_valid() and request.method == 'POST'):
        person = Penyedia.objects.get(superUser=request.user)
        vaksin = Vaksin.objects.all()
        jadwal = form.save(commit=False)
        jadwal.penyedia = person
        jadwal.save()
        vaksin.jumlah = int(jumlah1) - 1
        # vaksin.save()
        return HttpResponseRedirect('/profil-penerima/vaccine/ticket')
    else:
        form = VaccineForm()

    return render(request, 'tambahvaksin_index.html', {'form': form})

def load_tanggal(request):
    kota_id = request.GET.get('kota')
    tanggal = Vaksin.objects.filter(penyedia__kota=kota_id).values_list(
        'tanggal', flat=True).distinct()
    return render(request, 'hr/tanggal_dropdown.html', {'tanggal': tanggal})

def load_jenis_vaksin(request):
    tanggal_id = request.GET.get('tanggal')
    jenis_vaksin = Vaksin.objects.filter(tanggal=tanggal_id).values_list('jenis', flat=True).distinct()
    return render(request, 'hr/jenis_dropdown.html', {'jenis_vaksin': jenis_vaksin})

def load_tempat(request):
    jenis_id = request.GET.get('jenis_vaksin')
    tempat = Vaksin.objects.filter(jenis=jenis_id).exclude(jumlah=0).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})

@csrf_exempt
def penyedia_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        namaVaksin = data['namaVaksin']
        jumlah = data['jumlah']
        
        if namaVaksin and jumlah and username:
            Vaksin.objects.create(
                jenis = namaVaksin,
                jumlah = jumlah
            )

            response = {
                'msg':  'Vaksin berhasil ditambahkan!',
                'id' : 1
            }
        
        return JsonResponse(response)