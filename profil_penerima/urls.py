from django.urls import include, path
from .views import view_profile

urlpatterns = [
    path('', view_profile, name='view_profile'),
]