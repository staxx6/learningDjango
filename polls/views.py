from django.http import HttpResponse
<<<<<<< HEAD
from django.template import loader
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render,  get_object_or_404
from django.shortcuts import Http404
>>>>>>> 59429bb5830897f9178cd68f2b1b378fb3b33b6d

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
<<<<<<< HEAD
    return render(request, 'polls/detail.html', {'question':question})
=======
    return render(request, 'polls/detail.html', {'question': question})
>>>>>>> 59429bb5830897f9178cd68f2b1b378fb3b33b6d

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
