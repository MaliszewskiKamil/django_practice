from django.urls import path

from . import views

app_name = 'zelent'

urlpatterns = [
    path('', views.index, name='index'),
    path('html1/', views.html1, name='html1'),
    path('html2/', views.html2, name='html2'),
    path('css2/', views.css2, name='css2'),
    path('html3/welcome', views.html3, name='welcome'),
    path('html3/whoami', views.html3WhoAmI, name='whoami'),
    path('html3/offer', views.html3Offer, name='offer'),
    path('html3/contact', views.html3Contact, name='contact'),
    path('html3/cv', views.html3Cv, name='cv'),
    path('css3/', views.css3, name='css3')
]