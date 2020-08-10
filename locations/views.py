from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):

    a = 10
    html = ""
    for x in range(0,a+1):
        html = html + str(x)
    response = "<strong>This is the home page. </strong> %s"%html
    return HttpResponse(response)


# Create your views here.
