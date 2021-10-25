from django.shortcuts import redirect, render
from django.http import JsonResponse

from account.forms import RadioForm, PenyediaForm, PenerimaForm


def signup_radio(request):
    context = {}

    form = RadioForm(request.POST or None)

    # # Redirect to the lab-3 page
    if form.is_valid():
        if request.method == 'POST':
            selected = form.cleaned_data.get("role_choice")

            # Redirect ke form penyedia
            if selected == "penyedia":
                return redirect("/auth/signup/penyedia")
            # Redirect ke form penerima
            elif selected == "penerima":
                return redirect("/auth/signup/penerima")

    context['form'] = form
    return render(request, "signup_radio_button.html", context)


def signup_penyedia(request):
    context = {}

    form = PenyediaForm(request.POST or None)

    if form.is_valid():
        # Save the data
        form.save()

        if request.method == 'POST':
            return redirect('/auth/signup')

    context['form'] = form
    return render(request, "signup_penyedia.html", context)


def signup_penerima(request):
    context = {}

    form = PenerimaForm(request.POST or None)

    if form.is_valid():
        # Save the data
        form.save()

        if request.method == 'POST':
            return redirect('/auth/signup')

    context['form'] = form
    return render(request, "signup_penerima.html", context)
