from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForms(UserCreationForm):
    email = forms.EmailField(label = "Correo electronico")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class EditarUserForm(UserCreationForm):
    email = forms.EmailField(label = "Correo electronico")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    firstname = forms.CharField(label = "Modificar nombre")
    lastname = forms.CharField(label = "Modificar apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "firstname", "lastname"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label = "imagen")

class DescripcionForm(forms.Form):
    descripcion = forms.CharField(label = "descripcion", max_length = 300, widget = forms.Textarea)

class LinkForm(forms.Form):
    url = forms.URLField(label = "url")

    def __str__(self):
        return self.url