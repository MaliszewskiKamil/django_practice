from django.urls import path

from . import views

app_name = 'zelent'

urlpatterns = [
    path('', views.index, name='index'),
    path('html1/', views.html1, name='html1'),
    path('html2/', views.html2, name='html2'),
    path('css2/', views.css2, name='css2'),
]