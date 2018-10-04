from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    # Question클레스에 대한 QuesrySet을 가져옴
    # 게시일자 속성 에 대한 내림차순 순서로 최대 5개까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist') #쇼트컷이있다.
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # question_id가 pk인 Question 객체를 DB로부터 가져온 데이터로 생성
    # 만약 해당하는 Question이 없다면 Http404예외가 발생함
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 현재 투표중인 Question에 속한 Choice목록에서
        # pk가 POST 요청에 전달된 'choice' 값에 해당하는 Choice객체를 selected_choice변수에 할당
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 위의 try문에서 발생할 수 있는 예외는 2가지
        # 1. KeyError: request.POST에 'choice'키가 없을 때 발생
        # 2. Choice.DoesNotExist:
        #       question.choice_set.get(pk=무언가0에서 발생 (pk에 해당하는 객체가 DB까 없는 경우)
        return render(request, 'polls/detail.html', {
            #context가 들어가면 된다.
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
