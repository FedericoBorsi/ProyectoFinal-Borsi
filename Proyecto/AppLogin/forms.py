from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForms(UserCreationForm):
    correo = forms.EmailField(label = "Correo electronico")
    contraseña1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    contraseña2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["usermane", "correo", "contraseña1", "contraseña2"]
        help_text = {k: "" for k in fields}