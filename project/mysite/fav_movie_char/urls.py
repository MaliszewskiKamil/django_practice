from django.urls import path
from . import views

app_name = 'fav_movie_char'

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results')
]