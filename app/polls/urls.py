from django.urls import path
from . import views

# app_name = 'polls'
# urlpatterns = [
#     # /polls/a
#     path('', views.index, name='index'),
#     # r'(?P<question_id>\d+)/$'
#     path('<int:question_id>/', views.detail, name='datail'),
#     # r'(?P<question_id>\d+)/results/$'
#     path('<int:question_id>/results/',views.result, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
# from django.urls import path
#
from .views import fbv as views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]