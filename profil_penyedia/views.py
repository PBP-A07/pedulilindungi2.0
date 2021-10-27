from django.http.response import HttpResponseRedirect
from django.shortcuts import render
#from biodata.models import Penyedia
#from .forms import EditPenyediaForm

# Create your views here.
def profil_penyedia(request):
    #penyedia = Penyedia.objects.all()
    return render(request, 'profil_penyedia.html')

# def ubah_data_penyedia(request):
#     penyedia = Penyedia.objects.all()
#     form = EditPenyediaForm(request.POST or None, instance=penyedia)
#     if (form.is_valid and request.method == 'POST'):
#         form.save()
#         return HttpResponseRedirect('/profil-penyedia')
#     return render(request, 'ubah_data_penyedia.html')
