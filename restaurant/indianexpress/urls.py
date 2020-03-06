from django.contrib import admin
from django.conf.urls import url
from django.urls import path,re_path
from .import views

app_name = 'indianexpress'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    ]


