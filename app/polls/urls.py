from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path('test/', views.index, name='index'),
]