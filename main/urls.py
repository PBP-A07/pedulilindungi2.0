from django.urls import path
 
from . import views
 
app_name = 'main'
 
urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:id>', views.see_question, name='question'),
    path('question/<int:id>/json', views.get_responses, name='responses'),
    path('question/<int:id>/discussion/<int:id2>/json', views.get_responses2, name='responses'),
    path('reply', views.reply, name='reply'),
    path('json',  views.json, name='json'),
    path('json-flutter',  views.json_flutter, name='json-2'),
    path('json-account',  views.json_account_flutter, name='json-3'),
    path('post-question-flutter',  views.post_question_flutter, name='post-flutter'),
]
 

