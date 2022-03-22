from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('send-<str:email>-<str:username>/', views.send, name="send"),
]