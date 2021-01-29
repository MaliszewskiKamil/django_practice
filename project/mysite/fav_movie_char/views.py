from django.shortcuts import render
from django.http import request, HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Character

# Create your views here.

def index(request):
    movies_list = Movie.objects.all()
    context = {
        'movies_list': movies_list
    }
    return render(request, 'fav_movie_char/index.html', context)

def results(request):
    return render(request, 'vote succeded')

def vote(request):
    movies = get_list_or_404(Movie)
    for movie in movies:
        selected_char = movie.character_set.get(pk=request.POST[movie.title])
        selected_char.votes += 1
        selected_char.save()
    return HttpResponse('charpicker:results')


    