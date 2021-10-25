from django.shortcuts import render

# Create your views here.
def view_profile(request):
    return render(request, 'profile.html')