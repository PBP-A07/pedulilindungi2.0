from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from account.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers


def signup(request):
    context = {}

    form = CreateUserForm(request.POST)
    if form.is_valid():
        # Save user
        form.save()

        if request.method == 'POST':

            # Get data from forms.
            username = form.cleaned_data.get('username')
            selected = form.cleaned_data.get("role_choice")
            email = form.cleaned_data.get("email")

            # Edit the role.
            update_profile(request, username, selected, email)
            
            # login first time after signup
            return redirect('/auth/login-first/')

    context['form'] = form
    return render(request, "signup.html", context)


def update_profile(request, user_username, user_role, email):
    user = User.objects.get(username=user_username)
    user.profile.role = user_role
    user.profile.email = email
    user.save()


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Ke homepage setelah login.
            return redirect('/auth/afterLogin/')
    return render(request, 'login.html')

# Added login first time, after register redirect here
def login_first_time(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Ke homepage setelah login.
            if request.user.profile.role == 'penerima':
                return redirect('/biodata/peserta_form')
            elif request.user.profile.role == 'penyedia':
                return redirect('/biodata/penyedia_form')

    return render(request, 'login.html')


@login_required(login_url='login')
def afterLogin(request):
    response = {'user': request.user}
    return render(request, 'after_login.html', response)


def logout_user(request):
    logout(request)
    return redirect('/auth/login/')


def email_compare(request):
    User = get_user_model()
    users = User.objects.all()

    if request.is_ajax():
        email = request.POST.get("email")
        for user in users:
            if email == user.profile.email:
                return JsonResponse({"error": "Maaf, email tersebut sudah terdaftar di database."}, status=400)
    return JsonResponse({"success": "Email tersebut dapat digunakan."}, status=200)
