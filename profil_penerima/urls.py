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
    path('notes/delete/<id>', delete_message, name='delete_message'),
    path('notes/edit/<id>', edit_message, name='edit_message'),
    path('notes/load/template', load_template, name='msg_load_tempalte'),
    path('call/success', call_success, name='call_siccess'),
    path('call/failed', call_failed, name='call_failed'),
    path('vaccine/ticket', view_vaccine, name='vaccine_ticket'),
    path('vaccine/ticket/get', get_vaccine_ticket, name='get_vaccine'),
    path('vaccine/ticket/get/failed', get_vaccine_ticket_failed, name='get_vaccine_failed'),
    path('vaccine/delete/<id>', delete_vaccine, name='delete_vaccine'),
    path('user/flutter/<usn>', view_profile_flutter),
    path('profile/edit/flutter/<usn>', edit_profile_flutter),
    path('vaccine/flutter/get/<usn>', get_vaccine_flutter),
    path('vaccine/flutter/delete/<usn>', delete_vaccine_flutter),
]