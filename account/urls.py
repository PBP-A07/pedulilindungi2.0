from django.urls import path
from .views import signup_radio, signup_penyedia, signup_penerima

urlpatterns = [
    path('signup', signup_radio),
    path('signup/penyedia', signup_penyedia),
    path('signup/penerima', signup_penerima),
]
