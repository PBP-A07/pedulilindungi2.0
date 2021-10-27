from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from biodata.models import Peserta


def logout_account(request):
    auth_logout(request)
    return HttpResponseRedirect('/auth/login')
    

@login_required(login_url='/auth/login/')
def view_profile(request, usn):

    if request.user.username != usn and request.user.username != 'admin':
        return HttpResponseForbidden()

    elif request.user.profile.role == 'penyedia':
        # Change this to redirect to profile for penyedia
        return HttpResponseBadRequest()
    
    user = User.objects.get(username = request.user.username).profile
    print(request.user.profile)
    print(request.user)
    # penerima = Peserta.objects.get(NIK = user.nik)
    # 'penerima':penerima

    return render(request, 'profile.html', {'user':user, })