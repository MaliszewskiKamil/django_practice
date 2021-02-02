from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Article, Keywords
# Create your views here.

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list,
    }
    
    return render(request, 'blog/index.html', context)