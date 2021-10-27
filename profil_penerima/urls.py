from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get-msg', get_message, name='get_messages'),
    path('user/<usn>', view_profile, name='view_profile'),
    path('logout', logout_modal, name='logout_modal'),
    path('logout/confirm', logout_account, name='logout_account'),
    path('notes/add', create_message, name='create_message'),
    path('notes/delete/<id>', delete_message, name='create_message'),
    # path('notes/delete/confirm/<id>', delete_message, name='create_message'),
]