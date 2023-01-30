from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [ 
    path("", inicio, name = "inicio"),
    path("acercademi/", acercademi, name = "acercademi"),
    path("enviarmensaje/", enviarmensaje, name = "enviarmensaje"),
    path("mensaje/", mensaje, name = "mensaje"),
    path("casillamsj/", casillamsj, name = "casillamsj"),
    path("mostrarmsj/<id>", mostrarmsj, name = "mostrarmsj"),
    path("respondermsj/<id>", respondermsj, name = "respondermsj")

]