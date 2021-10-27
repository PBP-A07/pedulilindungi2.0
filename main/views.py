from django.core.checks import messages
from django.shortcuts import redirect, render

from main.models import Questions, Discussion
from .forms import NewQuestion, NewResponse, NewReply
from django.http import response


def home(request):
    questions = Questions.objects.all().order_by("-created_at")
    response = {'questions' : questions}

    # try : 
    if request.user.is_authenticated : 
        # if request.user.roles == "penerima" : 
        response["user"] = request.user
        return render(request, 'main/home_penerima.html', response)
    # except :     
    return render(request, 'main/home.html', response)

def new_question(request):
    form = NewQuestion(request.POST or None)

    if request.method == "POST" : 
        try : 
            form = NewQuestion(request.POST or None)
            if form.is_valid():
                questions = form.save(commit=False)
                questions.author = request.user
                questions.save()
                return response.HttpResponseRedirect('../#forum')
            
        except Exception as e:
            print(e) 
            
    context = {'form' : form}
    return render(request, "main/question.html", context)

def see_question(request, id) : 
    response_form = NewResponse(request.POST or None)
    reply_form = NewReply(request.POST or None)
    question = Questions.objects.get(id=id)

    if request.method == "POST" : 
        # print("error") 
        try : 
            response_form = NewResponse(request.POST or None)
            # print("sempat di sini")
            if response_form.is_valid():
                responses = response_form.save(commit=False)
                responses.author = request.user
                responses.forum = Questions(id=id)
                responses.save()
                return response.HttpResponseRedirect('../../')
            else : 
                print("error")

            
        except Exception as e:
            print(e)
            print("masuk siniiii")
    

    context = {
        "question" : question,
        "response_form" : response_form,
        "reply_form" : reply_form
    }
    return render(request, "main/detail_question.html", context)

def reply(request) : 
    if request.method == "POST" : 
        # print("error") 
        try : 
            reply_form = NewReply(request.POST or None)
            # print("sempat di sini")
            if reply_form.is_valid():
                question_id = request.POST.get("question")
                parent_id = request.POST.get("parent")
                reply = reply_form.save(commit=False)
                reply.author = request.user
                reply.forum = Questions(id=question_id)
                reply.parent = Discussion(id=parent_id)
                reply.save()
                return response.HttpResponseRedirect('question/' + str(question_id))
            else : 
                print("error")

            
        except Exception as e:
            print(e)
        
    
    return redirect('home')

