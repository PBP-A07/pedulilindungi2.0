from django.contrib.auth import logout
from django.urls import path
from .views import afterLogin, login_user, signup, logout_user, login_first_time

urlpatterns = [
    path('', signup),
    path('login/', login_user),
    path('afterLogin/', afterLogin),
    path('logout/', logout_user),
    path('login-first/', login_first_time),
]
