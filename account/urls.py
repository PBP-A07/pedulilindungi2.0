from django.contrib.auth import logout
from django.urls import path
from .views import afterLogin, email_compare, login_user, signup, logout_user

urlpatterns = [
    path('', signup),
    path('login/', login_user),
    path('afterLogin/', afterLogin),
    path('logout/', logout_user),
    path('email_compare', email_compare)
]
