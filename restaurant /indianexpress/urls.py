from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'indianexpress'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('reservation/', views.reservation, name="reservation"),
    path('menu/', views.menu, name="menu"),
    path('cart/', views.cart, name="cart"),
    path('gallery/', views.gallery, name="gallery"),
]


