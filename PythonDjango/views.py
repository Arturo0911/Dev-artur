from django.http import HttpResponse

def Saludo(request):
    return HttpResponse("<h1> Hola carevergas xD </h1>")