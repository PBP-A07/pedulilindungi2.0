from django.urls import include, path
from .views import view_profile, logout_account

urlpatterns = [
    path('user/<usn>', view_profile, name='view_profile'),
    path('logout', logout_account, name='logout_account'),
]