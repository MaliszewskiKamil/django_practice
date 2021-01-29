from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core import serializers
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
#from polls.models import Question, Choice

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     asjson = serializers.serialize('json', latest_question_list)
#     #return HttpResponse(asjson, content_type='application/json')
#     return render(request, "polls/index.html")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #haha = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/polls.html', context)


def zelentHTML1(request):
    return HttpResponse(request, 'zelent/zelentHTML1.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_for_this_question.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))