from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    #Question클레스에 대한 QuesrySet을 가져옴
    # 게시일자 속성 에 대한 내림차순 순서로 최대 5개까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist') #쇼트컷이있다.
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question,
    }
    return render(request, 'polls/detail.html', context)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
