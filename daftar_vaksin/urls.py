from django.urls import path
from .views import daftar_vaksin

urlpatterns = [
    path('', daftar_vaksin, name='daftar-vaksin')
]

