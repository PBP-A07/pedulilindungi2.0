from django.http.response import Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from biodata.models import Penyedia, Peserta
from daftar_vaksin.models import JadwalVaksin
from .models import CatatanPenyedia
from .forms import CatatanPenyediaForm, EditPenyediaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def index(request):
    return HttpResponseRedirect('/profil-penyedia/user/' + request.user.username)

@login_required(login_url='/auth/login/')
def profil_penyedia(request, usn):
    if request.user.username != usn:
        return HttpResponseForbidden("The Username does not match with yours")

    elif request.user.profile.role == 'penerima':
        return HttpResponseRedirect('/profil-penerima')

    elif request.user.profile.role != 'penyedia':
        return HttpResponseForbidden('Currently you have no role. Please contact the admin to assign you a role.')

    penyedia = Penyedia.objects.get(superUser = request.user)
    response = {'nama': penyedia.namaInstansi,
                'kota': penyedia.kota,
                'nomor_telepon': penyedia.nomorTelepon,
                'alamat': penyedia.alamat}
    return render(request, 'profil_penyedia.html', response)

@login_required(login_url='/auth/login/')
def ubah_data_penyedia(request):
    if request.user.profile.role != 'penyedia':
        return HttpResponseForbidden("You are not allowed to access this page because of your current role")

    penyedia = Penyedia.objects.get(superUser = request.user)
    form = EditPenyediaForm(request.POST or None, instance = penyedia)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/profil-penyedia')
    return render(request, 'ubah_data_penyedia.html', {'form': form})

@login_required(login_url='/auth/login/')
def catatan_penyedia(request):
    if request.user.profile.role != 'penyedia':
        return HttpResponseForbidden("You are not allowed to access this page because of your current role")

    notes = CatatanPenyedia.objects.filter(owner = request.user)
    if not notes:
        response = {'notes': None}
    else:
        notes_reversed = reversed(CatatanPenyedia.objects.filter(owner = request.user))
        response = {'notes': notes_reversed}
    return render(request, 'catatan_penyedia.html', response)

@login_required(login_url='/auth/login/')
def tambah_catatan(request):
    if request.user.profile.role != 'penyedia':
        return HttpResponseForbidden("You are not allowed to access this page because of your current role")

    form = CatatanPenyediaForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        f = form.save(commit=False)
        f.owner = User.objects.get(username = request.user.username)
        f.save()
        return HttpResponseRedirect('/profil-penyedia/catatan-penyedia')
    return render(request, 'form_catatan_penyedia.html')

@login_required(login_url='/auth/login/')
def lihat_pendaftar(request):
    if request.user.profile.role != 'penyedia':
        return HttpResponseForbidden("You are not allowed to access this page because of your current role")

    penyedia = Penyedia.objects.get(superUser = request.user)
    jenis = JadwalVaksin.objects.filter(place = penyedia).values('jenis_vaksin')
    tanggal = JadwalVaksin.objects.filter(place = penyedia).values('tanggal')
    penerima = JadwalVaksin.objects.filter(place = penyedia).values('penerima')
    list_orang = []
    dict_orang = dict()
    for i in range(penerima.count()):
        person = Peserta.objects.get(id = penerima[i].get('penerima'))
        dict_orang['nama']=person.namaLengkap
        dict_orang['nik']=person.NIK
        dict_orang['nomor_handphone']=person.nomorHandphone
        dict_orang['jenis_vaksin']=jenis[i].get('jenis_vaksin')
        dict_orang['tanggal']=tanggal[i].get('tanggal')
        list_orang.append(dict_orang.copy())
    list_orang.reverse()
    response = {'people': list_orang}
    return render(request, 'lihat_pendaftar.html', response)