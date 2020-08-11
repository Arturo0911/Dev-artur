from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question


def home_page(request):
    #response = "<strong>This is the home page. </strong>"
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    teamplate = loader.get_template('locations/index.html')

    context = {
        'lastest_question_list': lastest_question_list,
    }


    #output = ', '.join([q.question_text for q in lastest_question_list])
    #return HttpResponse(teamplate.render(context, request))
    return render(request,'locations/index.html', context )

def details_page(request, question_id_):

    question = get_object_or_404(Question, pk=question_id_)
    return render(request, 'locations/detail.html', {'question':question})

    """
    try:
        question = Question.objects.get(pk = question_id_)

    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    """
    

    #return render(request, 'polls/detail.html', {'question': question})

def results_page(request, question_id_):

    return HttpResponse("Estás buscando los resultados de la pregunta %s"%question_id_)

def vote(request, question_id_):

    return HttpResponse("Estás buscando los votos de la pregunta %s"%question_id_)



# Create your views here.
