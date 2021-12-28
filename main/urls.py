
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:id>', views.see_question, name='question'),
    path('reply', views.reply, name='reply'),
    path('json',  views.json, name='json'),
]
