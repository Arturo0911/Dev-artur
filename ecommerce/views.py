from django.shortcuts import render
#from django.http import 
# Create your views here.

def Search_products(request):
    return render(request, "products.html")