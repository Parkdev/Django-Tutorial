from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # r'(?P<question_id>\d+)/$'
    path('<int:question_id>/', views.detail, name='datail'),
    # r'(?P<question_id>\d+)/results/$'
    path('<int:question_id>/results/',views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]