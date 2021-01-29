from django.urls import path
from . import views

app_name = 'charpicker'

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results')
]