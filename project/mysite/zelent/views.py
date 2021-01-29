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