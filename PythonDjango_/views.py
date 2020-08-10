from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<div> <h5>This is the index page</h5>  </div>')


def detail(request, question_id):
    response = "this is your question %s. "%question_id
    return HttpResponse(response)

def results(request, question_id):
    response = "You're looking for results %s. "%question_id
    return HttpResponse(response)

def votes(request, question_id):
    response = "You are voting for questions %s. "%question_id
    return HttpResponse(response)



# Create your views here.
