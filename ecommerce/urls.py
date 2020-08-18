from django.urls import path

from . import views

urlpatterns = [
    path('', views.Search_products, name='index_products'),
]