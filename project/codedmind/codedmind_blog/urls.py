from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_detail, name="article_detail"),
    path('article/create/', views.article_create, name='article_create'),
    path('article_created/', views.article_created, name='article_created'),
]