from django.shortcuts import render
from AppLogin.views import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")

@login_required
def acercademi(request):
    return render(request, "acercademi.html")

@login_required
def enviarmensaje(request):
    if request.method == "POST":
        form = MensajeriaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info["receptor"]
            mensaje = info["mensaje"]
            fecha = info["fecha"]
            mensaje = Mensajeria(usuario = usuario, receptor = receptor, mensaje = mensaje, fecha = fecha)
            mensaje.save()
            return render(request, "inicio.html", {"mensaje": "El mensaje fue enviado correctamente"})
        else:
            return render(request, "enviarmensaje.html", {"form": form, "mensaje": "El mensaje no fue enviado correctamente"})
    else:
        form = MensajeriaForm()
        return render(request, "enviarmensaje.html", {"form": form})


@login_required
def mensaje(request):
    return render(request, "mensaje.html")


@login_required
def casillamsj(request):
    if request.user.is_authenticated:
        mensaje = Mensajeria.objects.filter(receptor = request.user)
        if len(mensaje) != 0:
            return render(request, "casillamsj.html", {"mensaje": mensaje})
        else:
            return render(request, "casillamsj.html", {"mensaje": "No hay mensajes"})


@login_required
def mostrarmsj(request, id):
    mensaje = Mensajeria.objects.get(id = id)
    mensaje.save()
    return render(request, "mostrarmsj.html", {"mensaje": mensaje})


@login_required
def respondermsj(request, id):
    mensaje = Mensajeria.objects.get(id = id)
    if request.method == "POST":
        form = MensajeriaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info["receptor"]
            mensaje = info["mensaje"]
            fecha = info["fecha"]
            mensaje = Mensajeria(usuario = usuario, receptor = receptor, mensaje = mensaje, fecha = fecha)
            mensaje.save()
            return render(request, "inicio.html", {"mensaje": "El mensaje fue enviado correctamente"})
        else:
            return render(request, "enviarmsj.html", {"form": form, "mensaje": "El mensaje no fue enviado"})
    else:
        form = MensajeriaForm()
        return render(request, "enviarmsj.html", {"form": form, "mensaje": mensaje})