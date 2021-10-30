from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get-msg', get_message, name='get_messages'),
    path('user/<usn>', view_profile, name='view_profile'),
    path('profile/edit', edit_profile, name='view_profile'),
    path('logout', logout_modal, name='logout_modal'),
    path('logout/confirm', logout_account, name='logout_account'),
    path('notes/add', create_message, name='create_message'),
    path('notes/delete/<id>', delete_message, name='create_message'),
    path('notes/edit/<id>', edit_message, name='create_message'),
    path('notes/load/template', load_template, name='create_message'),
    path('call/success', call_success, name='create_message'),
    path('call/failed', call_failed, name='create_message'),
    path('vaccine/ticket', view_vaccine, name='create_message'),
    path('vaccine/ticket/get', get_vaccine_ticket, name='create_message'),
    path('vaccine/ticket/get/failed', get_vaccine_ticket_failed, name='create_message'),
]