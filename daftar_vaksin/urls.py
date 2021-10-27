from django.urls import path
from .views import daftar_vaksin, load_tempat

urlpatterns = [
    path('', daftar_vaksin, name='daftar-vaksin'),
    path('ajax/load-tempat', load_tempat, name='ajax-load-tempat')
]

