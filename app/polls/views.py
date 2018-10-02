from django.http import HttpResponse
from .models import Question
from django.shortcuts import render


# Create your views here.

def index(request):
    #Question클레스에 대한 QuesrySet을 가져옴
    # 게시일자 속성 에 대한 내림차순 순서로 최대 5개까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #order_by('-xxx')에서 - 가 붙으면 내림차순을 뜻한다.[:5] 최대 5개까지

    # 가져온 Question QuerySet을 사용, 각 Question의 question_text속성값들을 list comprehension을 사용해 리스트로 생성
    # 생성된 리스트를 ', ' 문자열의 join메서드의 인수로 전달, output에 쉼표단위로 연결된 문자열을 할
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
