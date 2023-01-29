from django.shortcuts import render
from AppLogin.views import *

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")

def acercademi(request):
    return render(request, "acercademi.html")


