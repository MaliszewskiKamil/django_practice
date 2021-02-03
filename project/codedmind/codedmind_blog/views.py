from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from .models import Article, Keywords
# Create your views here.

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list,
    }
    
    return render(request, 'blog/index.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'blog/post.html', context)

def article_create(request):
    return render(request, 'blog/create.html')

def article_created(request):
    title = request.GET['title']
    img_path = request.GET['img_path']
    article = request.GET['article']
    Article(title=title, img_path=img_path, article=article).save()
    return HttpResponseRedirect(reverse('blog:index'))