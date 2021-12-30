from django.http import response
from django.http.response import Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators import csrf
from biodata.models import Peserta
from django.core import serializers
import datetime
import json

from django.views.decorators.csrf import csrf_exempt
import json as JSON

from daftar_vaksin.models import JadwalVaksin
from .forms import *

from profil_penerima.models import Message

@login_required(login_url='/auth/login/')
def index(request):
    return HttpResponseRedirect('/profil-penerima/user/' + request.user.username)

def logout_account(request):
    auth_logout(request)
    return HttpResponseRedirect('/auth/login')

def logout_modal(request):
    return render(request, 'logout-modal.html')
    
@login_required(login_url='/auth/login/')
def view_profile(request, usn):

    if request.user.username != usn:
        return HttpResponseForbidden("The Username does not match with yours")

    elif request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseRedirect('/profil-penyedia')
    
    elif request.user.profile.role != 'penerima':
        return HttpResponseForbidden('Currently you have no role. Please contact the admin to assign you a role.')
    
    user = User.objects.get(username = request.user.username).profile
    penerima = Peserta.objects.get(superUser = request.user)
    JadwalVaksin.objects.filter(tanggal__lt=datetime.date.today()).delete()

    return render(request, 'profile.html', {'user':user, 'penerima':penerima})

@csrf_exempt
def view_profile_flutter(request, usn):
    user = User.objects.get(username = usn).profile
    penerima = Peserta.objects.get(superUser = User.objects.get(username = usn))
    JadwalVaksin.objects.filter(tanggal__lt=datetime.date.today()).delete()

    data = serializers.serialize('json', [user, penerima,])
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='/auth/login/')
def get_message(request):
    messageObjs = Message.objects.filter(creator = request.user)

    if messageObjs:
        data = serializers.serialize('json', messageObjs)
        return HttpResponse(data, content_type="application/json")

    response = {
        'id' : -1
    }
    return JsonResponse(response)

@login_required(login_url='/auth/login/')
def create_message(request):
    form = MessageForm(request.POST or None)

    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()

    if (form.is_valid() and request.method == 'POST'):
        # save the form data to model
        tempMsgObj = form.save(commit=False)
        tempMsgObj.creator = User.objects.get(username = request.user.username)
        tempMsgObj.save()

        # when saved json dump
        response = {
            'url' : '/profil-penerima'
        }
        return JsonResponse(response)
    
    return render(request, 'add-message-modal.html', {'form': form})

@login_required(login_url='/auth/login/')
def delete_message(request, id):

    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()

    try:
        note = Message.objects.get(id = id)

        if(request.method == 'POST'):
            note.delete()
            return JsonResponse({'url':'/profil-penerima'})
        
    except Message.DoesNotExist:
        return Http404
    
    return render(request, 'delete-message-modal.html', {'message':note})

@login_required(login_url='/auth/login/')
def edit_message(request, id):
    
    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()

    try:
        note = Message.objects.get(id = id)
        form = MessageForm(request.POST or None, instance = note)

        if note.creator != User.objects.get(username = request.user.username):
            return HttpResponseForbidden()

        if (form.is_valid() and request.method == 'POST'):
            # save the form data to model
            form.save()
            return JsonResponse({'url' : '/profil-penerima'})
        
    except Message.DoesNotExist:
        return Http404
    
    return render(request, 'edit-message-modal.html', {'form':form, 'message':note})

@login_required(login_url='/auth/login/')
def edit_profile(request):
    
    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()

    try:
        user = User.objects.get(username = request.user.username)
        penerima = Peserta.objects.get(superUser = user)
        form = PenerimaForm(request.POST or None, instance = penerima)
        # formUser = UserForm(request.POST or None, instance = user.profile)

        if (form.is_valid() and request.method == 'POST'):
            # save the form data to model
            form.save()
            # formUser.save()
            return JsonResponse({'url' : '/profil-penerima'})
        elif (not form.is_valid() and request.method == 'POST'):
            return JsonResponse({'url' : '/profil-penerima', 'id':-1})
        
    except Peserta.DoesNotExist:
        return Http404
    
    return render(request, 'profile-edit.html', {'form':form, 'user':penerima, 'userProf':user})

@csrf_exempt
def edit_profile_flutter(request, usn):

    response = {}

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        namaLengkap = data['namaLengkap']  
        nik = data['nik']  
        tanggalLahir = data['tanggalLahir']
        jenisKelamin = data['jenisKelamin']
        nomorHandphone = data['nomorHandphone']
        alamat = data['alamat']
        # Updated Here: Added superUser
        username = data['username']

        if namaLengkap and nik and tanggalLahir and jenisKelamin and nomorHandphone and alamat and username:
            penerima = Peserta.objects.get(superUser = User.objects.get(username = usn))
            form = PenerimaForm(request.POST or None, instance = penerima)

            temp = form.save(commit = False)

            temp.namaLengkap = namaLengkap
            temp.NIK = nik
            temp.tanggalLahir = tanggalLahir
            temp.jenisKelamin = jenisKelamin
            temp.nomorHandphone = nomorHandphone
            temp.alamat = alamat

            temp.save()

            response = {
                'msg':  'Biodata Anda berhasil disimpan!',
                'id' : 1
            }

    return JsonResponse(response)

def load_template(request):
    
    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()
    
    return render(request, 'notes-template.html')

def call_success(request):
    return render(request, 'success-modal.html')

def call_failed(request):
    return render(request, 'failed-modal.html')

@csrf_exempt
def get_vaccine_flutter(request, usn):
    JadwalVaksin.objects.filter(tanggal__lt=datetime.date.today()).delete()
    penerima = Peserta.objects.get(superUser = User.objects.get(username = usn))
    try:
        vaccine = JadwalVaksin.objects.get(penerima = penerima)

        data = serializers.serialize('json', [penerima, vaccine, ])
        return HttpResponse(data, content_type="application/json")

    except JadwalVaksin.DoesNotExist:
        return JsonResponse({'id' : -1})

@login_required(login_url='/auth/login/')
def view_vaccine(request):

    if request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseRedirect('/profil-penyedia')
    
    elif request.user.profile.role != 'penerima':
        return HttpResponseForbidden('Currently you have no role. Please contact the admin to assign you a role.')
    
    user = User.objects.get(username = request.user.username).profile
    penerima = Peserta.objects.get(superUser = request.user)
    JadwalVaksin.objects.filter(tanggal__lt=datetime.date.today()).delete()

    return render(request, 'vaccine-ticket.html', {'user':user, 'penerima':penerima})

@login_required(login_url='/auth/login/')
def get_vaccine_ticket(request):

    if request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseRedirect('/profil-penyedia')
    
    elif request.user.profile.role != 'penerima':
        return HttpResponseForbidden('Currently you have no role. Please contact the admin to assign you a role.')

    # user = User.objects.get(username = request.user.username).profile
    penerima = Peserta.objects.get(superUser = request.user)
    JadwalVaksin.objects.filter(tanggal__lt=datetime.date.today()).delete()

    # Uncomment and finish this after JadwalVaksin is fixed
    try:
        vaccine = JadwalVaksin.objects.get(penerima = penerima)

        data = serializers.serialize('json', [penerima, vaccine, ])
        return HttpResponse(data, content_type="application/json")

    except JadwalVaksin.DoesNotExist:
        return JsonResponse({'id' : -1})

@login_required(login_url='/auth/login/')
def get_vaccine_ticket_failed(request):

    if request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseRedirect('/profil-penyedia')
    
    elif request.user.profile.role != 'penerima':
        return HttpResponseForbidden('Currently you have no role. Please contact the admin to assign you a role.')

    return render(request, 'vaccine-ticket-card-failed.html')

@login_required(login_url='/auth/login/')
def delete_vaccine(request, id):

    if request.user.profile.role != 'penerima':
        return HttpResponseForbidden()

    try:
        penerima = Peserta.objects.get(superUser = request.user)
        vaccine = JadwalVaksin.objects.get(penerima = penerima)

        if(request.method == 'POST'):
            vaccine.delete()
            return JsonResponse({'url':'/profil-penerima'})
        
    except JadwalVaksin.DoesNotExist:
        return Http404
    
    return render(request, 'delete-vaccine-modal.html', {'vaccine':vaccine})

@csrf_exempt
def delete_vaccine_flutter(request, usn):
    response = {
                'msg':  'Tikat anda berhasil dihapus',
                'id' : 1
            }

    try:
        penerima = Peserta.objects.get(superUser = User.objects.get(username = usn))
        vaccine = JadwalVaksin.objects.get(penerima = penerima)

        if(request.method == 'POST'):
            vaccine.delete()
            return JsonResponse(response)
        
    except JadwalVaksin.DoesNotExist:
        return JsonResponse({
                'msg':  'Tikat anda gagal dihapus',
                'id' : 1
            })
    return JsonResponse(response)