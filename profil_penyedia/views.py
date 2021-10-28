from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import render
from biodata.models import Penyedia
from .models import CatatanPenyedia
from .forms import CatatanPenyediaForm, EditPenyediaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def profil_penyedia(request):
    penyedia = Penyedia.objects.get(superUser = request.user)
    response = {'nama': penyedia.namaInstansi,
                'kota': penyedia.kota,
                'nomor_telepon': penyedia.nomorTelepon,
                'alamat': penyedia.alamat}
    return render(request, 'profil_penyedia.html', response)

@login_required(login_url='/auth/login/')
def ubah_data_penyedia(request):
    penyedia = Penyedia.objects.get(superUser = request.user)
    form = EditPenyediaForm(request.POST or None, instance = penyedia)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/profil-penyedia')
    return render(request, 'ubah_data_penyedia.html')

@login_required(login_url='/auth/login/')
def lihat_pendaftar(request):
    return render(request, 'lihat_pendaftar.html')

@login_required(login_url='/auth/login/')
def catatan_penyedia(request):
    notes = CatatanPenyedia.objects.filter(owner = request.user)
    response = {'notes': notes}
    return render(request, 'catatan_penyedia.html', response)

@login_required(login_url='/auth/login/')
def tambah_catatan(request):
    form = CatatanPenyediaForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        f = form.save(commit=False)
        f.owner = User.objects.get(username = request.user.username)
        f.save()
        return HttpResponseRedirect('/profil-penyedia/catatan-penyedia')
    return render(request, 'form_catatan_penyedia.html')
