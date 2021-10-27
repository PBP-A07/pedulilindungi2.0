from django.contrib.auth import logout
from django.urls import path
from .views import afterLogin, login_user, signup, logout_user, login_first_time, email_compare

urlpatterns = [
    path('', signup),
    path('login/', login_user),
    path('afterLogin/', afterLogin),
    path('logout/', logout_user),
    path('email_compare', email_compare),
    path('login-first/', login_first_time),
]
