from django import views
from django.contrib import admin 
from django.urls import path 
from . import views
# from .views import sayHello 
  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', views.index, name='index')
]