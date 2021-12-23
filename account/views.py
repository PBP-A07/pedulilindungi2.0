from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from account.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    context = {}

    # Kalo udah ada user yang login, langsung arahin ke home setelah login.
    if request.user.is_authenticated:
        return redirect('/#/')

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


@csrf_exempt
def flutter_signup(request):
    if request.method != "POST":
        return JsonResponse({"result": "Must use POST method!"})

    if not request.body:
        return JsonResponse({"result": "Must provide request body!"})

    data = json.loads(request.body)
    email = data["email"]
    username = data["username"]
    password = data["password"]
    selected = data["role"]

    if not email or not username or not password:
        return JsonResponse({"result": "Must provide email, username, and password"})

    form = CreateUserForm({
        'username': username,
        'email': email,
        'password1': password,
        'password2': password,
        'role_choice': selected,
    })

    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        if form.is_valid():
            form.save()

            # Edit the role.
            update_profile(request, username, selected, email)

            return JsonResponse({"result": "Sign up success!"})

        return JsonResponse({"result": "Sign up data not valid!"})

    return JsonResponse({"result:" "This username already exist!"}, status=400)


def update_profile(request, user_username, user_role, email):
    user = User.objects.get(username=user_username)
    user.profile.role = user_role
    user.profile.email = email
    user.save()


@csrf_exempt
def login_user(request):
    # Kalo udah ada user yang log in, langsung arahin ke home setelah login.
    if request.user.is_authenticated:
        return redirect('/#/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Ke homepage setelah login.
            return redirect('/#/')
        else:
            messages.error(request, "Your username or password is wrong!")

    return render(request, 'login.html')

# Added login first time, after register redirect here.


@csrf_exempt
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
        else:
            messages.error(request, "Your username or password is wrong!")

    return render(request, 'login.html')


@csrf_exempt
def flutter_login(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]

    user = authenticate(request, username=username, password=password)
    if (user is not None):
        print("Not None")
        return JsonResponse({"message": "You're logged in successfully!", "username": username}, status=200)
    else:
        print("None")
        return JsonResponse({"message": "Your password or username is wrong!"}, status=404)


def logout_user(request):
    logout(request)
    return redirect('/#/')


def email_compare(request):
    User = get_user_model()
    users = User.objects.all()

    if request.is_ajax():
        email = request.POST.get("email")
        for user in users:
            if email == user.profile.email:
                return JsonResponse({"error": "Maaf, email tersebut sudah terdaftar di database."}, status=400)
    return JsonResponse({"success": "Email tersebut dapat digunakan."}, status=200)
