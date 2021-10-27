from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from biodata.models import Penyedia
from .forms import EditPenyediaForm

# Create your views here.
# versi 1
# def profil_penyedia(request):
#     response = {'nama': request.user.profile.namaInstansi,
#                 'kota': request.user.profile.kota,
#                 'nomor_telepon': request.user.profile.nomorTelepon,
#                 'alamat': request.user.profile.alamat}
#     return render(request, 'profil_penyedia.html', response)

#versi 2
# def profil_penyedia(request):
#     penyedia = User.objects.get(username=request.user.username)
#     response = {'nama': penyedia.profile.namaInstansi,
#                 'kota': penyedia.profile.kota,
#                 'nomor_telepon': penyedia.profile.nomorTelepon,
#                 'alamat': penyedia.profile.alamat}
#     return render(request, 'profil_penyedia.html', response)

#versi 3
def profil_penyedia(request):
    response = {'x': User.objects.get(username=request.user.username)}
    return render(request, 'profil_penyedia.html', response)

def ubah_data_penyedia(request):
    penyedia = Penyedia.objects.all()
    form = EditPenyediaForm(request.POST or None, instance=penyedia)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/profil-penyedia')
    return render(request, 'ubah_data_penyedia.html')
