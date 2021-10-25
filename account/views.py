from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import JsonResponse
from account.forms import CreateUserForm


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
            # return redirect('/login')

    context['form'] = form
    return render(request, "signup.html", context)


def update_profile(request, user_username, user_role, email):
    user = User.objects.get(username=user_username)
    user.profile.role = user_role
    user.profile.email = email
    user.save()
