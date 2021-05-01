from django.contrib import admin
from django.urls import path
from . import views

# Code here

urlpatterns = [
    path('',views.home,name="home"),

    path('', views.post_opinion, name='post_opinion'),
    
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
]