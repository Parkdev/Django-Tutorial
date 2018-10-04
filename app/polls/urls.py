from django.urls import path, include
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
from .views import cbv, fbv as views
app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # /polls/cbv/로 시작하는 URL요청은
    # 위의 urlpatterns_cbv리스트 내의 내요엥서 처리
    path('cbv/', include(urlpatterns_cbv))
]