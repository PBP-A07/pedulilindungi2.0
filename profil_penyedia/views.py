from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import render
from biodata.models import Penyedia
# from .forms import EditPenyediaForm
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

# def ubah_data_penyedia(request):
#     penyedia = Penyedia.objects.all()
#     form = EditPenyediaForm(request.POST or None, instance=penyedia)
#     if (form.is_valid and request.method == 'POST'):
#         form.save()
#         return HttpResponseRedirect('/profil-penyedia')
#     return render(request, 'ubah_data_penyedia.html')
