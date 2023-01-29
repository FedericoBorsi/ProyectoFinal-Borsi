from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path("register/", register, name = "register"),
    path("login/", login_request, name = "login"),
    path("logout/", LogoutView.as_view(), name = "logout"),
    path("editarPerfil/", editarperfil, name = "editarPerfil"),
    path("perfil/", perfil, name = "perfil"),
    path("agregaravatar/", agregar_avatar, name ="agregaravatar"),
    path("agregarurl/", agregar_url, name = "agregarurl"),
    path("agregardescripcion/", agregar_descripcion, name = "agregardescripcion")
]