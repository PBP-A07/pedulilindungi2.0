from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import PesertaForm, PenyediaForm
from .models import *

def index(request):
    response = {}
    return render(request, 'index_PTS.html', response)

# @login_required(login_url='/admin/login/')
def biodata_peserta(request):
    context ={}
  
    # create object of form
    form = PesertaForm(request.POST or None, label_suffix="") # label_suffix="" -> ilangin titik-dua (:) untuk field
      
    # check if form data is valid
    if (form.is_valid and request.method == 'POST'):
        # save the form data to model
        form.save()

        # Get data from forms.
        namaLengkap = form.cleaned_data.get("namaLengkap")
        nik = form.cleaned_data.get("nik")
        tanggalLahir = form.cleaned_data.get("tanggalLahir")
        jenisKelamin = form.cleaned_data.get("jenisKelamin")
        nomorHandphone = form.cleaned_data.get("nomorHandphone")
        alamat = form.cleaned_data.get("alamat")

        update_profile_peserta(request, request.user.username, namaLengkap, nik, tanggalLahir, jenisKelamin, nomorHandphone, alamat)

        return HttpResponseRedirect('/biodata')
  
    context['form']= form
    return render(request, "peserta_form.html", context)

# @login_required(login_url='/admin/login/')
def biodata_penyedia(request):
    context ={}
  
    # create object of form
    form = PenyediaForm(request.POST or None, label_suffix="") # label_suffix="" -> ilangin titik-dua (:) untuk field
      
    # check if form data is valid
    if (form.is_valid and request.method == 'POST'):
        # save the form data to model
        form.save()

        # Get data from forms.
        instansi = form.cleaned_data.get("namaInstansi")
        kota = form.cleaned_data.get("kota")
        telepon = form.cleaned_data.get("nomorTelepon")
        alamat = form.cleaned_data.get("alamat")

        update_profile_penyedia(request, request.user.username, instansi, kota, telepon, alamat)

        return HttpResponseRedirect('/biodata')
  
    context['form']= form
    return render(request, "penyedia_form.html", context)

def update_profile_penyedia(request, user_username, namaInstansi, kota, telepon, alamat):
    user = User.objects.get(username=user_username)
    user.profile.namaInstansi = namaInstansi
    user.profile.kota = kota
    user.profile.nomorTelepon = telepon
    user.profile.alamat = alamat
    user.save()

def update_profile_peserta(request, user_username, namaLengkap, nik, tanggalLahir, jenisKelamin, nomorHandphone, alamat):
    user = User.objects.get(username=user_username)
    user.profile.namaLengkap = namaLengkap
    user.profile.nik = nik
    user.profile.tanggalLahir = tanggalLahir
    user.profile.jenisKelamin = jenisKelamin
    user.profile.nomorHandphone = nomorHandphone
    user.profile.alamat = alamat
    user.save()

def ajax_posting_peserta(request):
    if request.method == 'POST':
        namaLengkap = request.POST['namaLengkap']  
        nik = request.POST['nik']  
        tanggalLahir = request.POST['tanggalLahir']
        jenisKelamin = request.POST['jenisKelamin']
        nomorHandphone = request.POST['nomorHandphone']
        alamat = request.POST['alamat']
        
        if namaLengkap and nik and tanggalLahir and jenisKelamin and nomorHandphone and alamat:
            Peserta.objects.create(
                namaLengkap = namaLengkap, 
                NIK = nik,
                tanggalLahir = tanggalLahir,
                jenisKelamin = jenisKelamin,
                nomorHandphone = nomorHandphone,
                alamat = alamat
            )

            response = {
                'msg':  'Biodata Anda berhasil disimpan!',
                'id' : 1
            }
        
        else :
            response = {
                'msg':  'Silahkan isi form dengan benar!',  # response message
                'id' : 2
            }
        return JsonResponse(response)

def ajax_posting_penyedia(request):
    if request.method == 'POST':
        namaInstansi = request.POST['namaInstansi']  
        kota = request.POST['kota'] 
        nomorTelepon = request.POST['nomorTelepon']
        alamat = request.POST['alamat']
        
        if namaInstansi and kota and nomorTelepon and alamat:
            Penyedia.objects.create(
                namaInstansi = namaInstansi, 
                kota = kota,
                nomorTelepon = nomorTelepon,
                alamat = alamat
            )

            response = {
                'msg':  'Informasi instansi Anda berhasil disimpan!',
                'id' : 1
            }
        
        else :
            response = {
                'msg':  'Silahkan isi form dengan benar!', 
                'id' : 2
            }
        return JsonResponse(response)