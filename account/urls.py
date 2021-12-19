from django.contrib.auth import logout
from django.urls import path
from .views import login_user, signup, logout_user, login_first_time, email_compare, flutter_login

urlpatterns = [
    path('', signup),
    path('login/', login_user),
    path('logout/', logout_user),
    path('email_compare', email_compare),
    path('login-first/', login_first_time),
    path('flutter-login/', flutter_login),
]
