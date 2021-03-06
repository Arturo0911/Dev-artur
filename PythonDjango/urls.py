"""PythonDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from PythonDjango.views import Saludo
#from PythonDjango_.views import index
#from . import views
from ecommerce import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('PythonDjango_.urls')),
    path('home/', include('locations.urls')),
    path('product', include('ecommerce.urls'),)
    #path('products/', views.Search_products),
    #path('products/', views.search),
    #path('', index, name= 'index'), # to declare the index page it's not neccessary use '/', only single quotes to indicate like this ''
]
    