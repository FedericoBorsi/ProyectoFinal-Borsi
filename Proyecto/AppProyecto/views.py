from django.shortcuts import render
from AppLogin.views import *

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")