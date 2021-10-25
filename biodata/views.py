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
        return HttpResponseRedirect('/biodata')
  
    context['form']= form
    return render(request, "penyedia_form.html", context)

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