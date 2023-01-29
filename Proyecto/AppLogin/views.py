from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegisterUserForms, EditarUserForm, LinkForm, DescripcionForm, AvatarForm
from .models import Avatar, Link, Descripcion
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje": f"El usuario {username} fue creado correctamente"})
        else:
            return render(request, "inicio.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form = RegisterUserForms()
        return render(request, "register.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info["username"]
            contra = info["password"]
            usuario = authenticate(username = usu, password = contra)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje": f"El usuario {usu} inicio sesión correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje": "Usuario o contraseña incorrecto"})
        else:
            return render(request, "login.html", {"form": form, "mensaje": "Usuario o contraseña incorrecto"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

@login_required
def editarperfil(request):
    usuario = request.user

    if request.method == "POST":
        form = EditarUserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.firstname = info["firstname"]
            usuario.lastname = info["lastname"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje": f"El usuario {usuario.username} fue modificado correctamente"})
        else:
            return render(request, "editarperfil.html", {"form": form, "nombredeusuario": usuario.username})

    else:
        form = EditarUserForm(instance = usuario)
        return render(request, "editarperfil.html", {"form": form, "nombreusuario": usuario.username})


def obtener_avatar(request):
    lista = Avatar.objects.filter(usuario = request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = "/media/Avatars/default.png"
    return avatar


def obtener_url(request):
    lista = Link.objects.filter(usuario = request.user)
    if len(lista) != 0:
        url = lista[0].url
    else:
        url = ""
    return url

    
def obtener_descripcion(request):
    lista = Descripcion.objects.filter(usuario = request.user)
    if len(lista) != 0:
        descripcion = lista[0].descripcion
    else:
        descripcion = ""
    return descripcion


@login_required
def agregar_avatar (request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(usuario = request.user, imagen = request.FILES["imagen"])
            avatar_actual= Avatar.objects.filter(usuario = request.user)
            if len(avatar_actual)>0:
                avatar_actual[0].delete()
            avatar.save()
            return render (request, "perfil.html", {"form": form, "avatar": obtener_avatar(request), "mensaje": "Avatar agregado/cambiado con exito"})
        else:
            return render (request, "perfil.html", {"form": form, "avatar": obtener_avatar(request), "mensaje": "Error al agregar/cambiar el avatar"})
    else:
        form = AvatarForm()
        return render(request, "agregaravatar.html", {"form": form, "avatar": obtener_avatar(request), "mensaje": "Agregar o cambiar tu avatar"})


@login_required
def agregar_url (request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            url = Link(usuario = request.user, url = request.POST["url"])
            link_actual= Link.objects.filter(usuario = request.user)
            if len(link_actual)>0:
                link_actual[0].delete()
            url.save()
            return render (request, "perfil.html", {"form": form, "url" : obtener_url(request), "mensaje": "Link agregado/cambiado con exito", "avatar": obtener_avatar(request), "url": obtener_url})
        else:
            return render (request, "agregarlink.html", {"form": form, "mensaje": "Error al agregar/cambiar el link", "avatar": obtener_avatar(request)})
    else:
        form = LinkForm()
        return render(request, "agregarlink.html", {"form": form})


@login_required
def agregar_descripcion (request):
    if request.method == "POST":
        form = DescripcionForm(request.POST)
        if form.is_valid():
            descripcion = Descripcion(usuario = request.user, descripcion = request.POST["descripcion"])
            descripcion_actual= Descripcion.objects.filter(usuario = request.user)
            if len(descripcion_actual)>0:
                descripcion_actual[0].delete()
            descripcion.save()
            return render (request, "perfil.html", {"form": form, "mensaje": "Descripcion agregada/cambiada con exito", "descripcion": obtener_descripcion(request), "avatar": obtener_avatar(request)})
        else:
            return render (request, "perfil.html", {"form": form, "mensaje": "Error al agregar/cambiar la descripcion", "avatar": obtener_avatar(request)})
    else:
        form = DescripcionForm()
        return render(request, "agregardescripcion.html", {"form": form})


@login_required
def perfil(request):
    usuario = request.user
    form = EditarUserForm(instance = usuario)
    return render(request, "perfil.html", {"form": form, "avatar": obtener_avatar(request), "url": obtener_url(request), "descripcion": obtener_descripcion(request)})