from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core import serializers
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(request, "Index")

def html1(request):
    context = {}
    return render(request, 'tutorial/html/episode1/index.html')

def html2(request):
    context = {}
    return render(request, 'tutorial/html/episode2/divs.html')

def css2(request):
    return render(request, 'tutorial/css/css2/index.html')

def css3(request):
    return render(request, 'tutorial/css/css3/index.html')

def html3(request):
    return render(request, 'tutorial/html/episode3/index.html')

def html3WhoAmI(request):
    return render(request, 'tutorial/html/episode3/whoami.html')

def html3Offer(request):
    return render(request, 'tutorial/html/episode3/offer.html')

def html3Contact(request):
    return render(request, 'tutorial/html/episode3/contact.html')

def html3Cv(request):
    return render(request, 'tutorial/html/episode3/cv.html')
