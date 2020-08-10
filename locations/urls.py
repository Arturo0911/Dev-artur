from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('<int:question_id_>/', views.details_page, name= "details"),
    path('<int:question_id_>/results/', views.results_page, name= "results"),
    path('<int:question_id_>/vote/', views.vote, name= "vote"),
]