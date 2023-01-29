from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [ 
    path("", inicio, name = "inicio"),
    path("acercademi/", acercademi, name = "acercademi"),
]