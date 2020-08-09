from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    return HttpResponse("<h1> Holi arturón  xD </h1>")
# Create your views here.
