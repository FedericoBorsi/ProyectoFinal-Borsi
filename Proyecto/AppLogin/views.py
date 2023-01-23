from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterUserForms

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "AppProyecto/inicio.html", {"mensaje": f"El usuario {username} fue creado correctamente"})
        else:
            return render(request, "register.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form = RegisterUserForms()
        return render(request, "register.html", {"form": form})