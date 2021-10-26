from django.contrib.auth import logout
from django.urls import path
from .views import afterLogin, login_user, signup, logout_user

urlpatterns = [
    path('', signup),
    path('login/', login_user),
    path('afterLogin/', afterLogin),
    path('logout/', logout_user)
]
